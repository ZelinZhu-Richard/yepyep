"""Validated, explicitly estimated model pricing. Standard library only."""

import hashlib
import json
import math
from datetime import datetime, timezone

SOURCE_URL = "https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json"
PROVIDERS = {"openai", "anthropic"}
STALE_AFTER_DAYS = 7   # weekly refresh cadence: older data is ranked but labeled
MAX_AGE_DAYS = 30      # beyond this the estimate is refused


def positive_number(value):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and value > 0)


def parse_time(value):
    if not isinstance(value, str):
        raise ValueError("Missing retrieval timestamp")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("Invalid retrieval timestamp") from exc
    if parsed.tzinfo is None:
        raise ValueError("Retrieval timestamp needs a timezone")
    return parsed


def validate_catalog(data):
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("Unsupported catalog schema")
    if data.get("price_basis") != "community_reported_direct_api_standard_uncached":
        raise ValueError("Unexpected price basis")
    parse_time(data.get("fetched_at"))
    source = data.get("source", {})
    if not isinstance(source, dict) or source.get("url") != SOURCE_URL:
        raise ValueError("Unexpected source")
    digest = source.get("sha256", "")
    if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
        raise ValueError("Missing source digest")
    rows = data.get("models")
    if not isinstance(rows, list) or not rows:
        raise ValueError("Empty model catalog")
    seen, providers = set(), set()
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Malformed model entry")
        model_id = row.get("id")
        if not isinstance(model_id, str) or not model_id.strip() or model_id in seen:
            raise ValueError("Missing or duplicate model ID")
        seen.add(model_id)
        if row.get("provider") not in PROVIDERS:
            raise ValueError("Unexpected provider")
        providers.add(row["provider"])
        for field in ("input_usd_per_million", "output_usd_per_million"):
            if not positive_number(row.get(field)):
                raise ValueError(f"Invalid price for {model_id}: {field}")
    if providers != PROVIDERS:
        raise ValueError("Catalog must contain both OpenAI and Anthropic")
    return data


def normalize(raw, now=None):
    feed = json.loads(raw)
    if not isinstance(feed, dict):
        raise ValueError("Upstream feed must be an object")
    rows = []
    skipped = 0
    for model_id, entry in sorted(feed.items()):
        if not isinstance(entry, dict) or entry.get("mode") != "chat" or entry.get("litellm_provider") not in PROVIDERS:
            continue
        input_price = entry.get("input_cost_per_token")
        output_price = entry.get("output_cost_per_token")
        if isinstance(input_price, bool) or isinstance(output_price, bool):
            raise ValueError(f"Invalid upstream price for {model_id}")
        if input_price is None or output_price is None or input_price == 0 or output_price == 0:
            # Missing/free promotional prices cannot establish a paid-worker ranking.
            skipped += 1
            continue
        if not positive_number(input_price) or not positive_number(output_price):
            raise ValueError(f"Invalid upstream price for {model_id}")
        rows.append({
            "id": model_id,
            "provider": entry["litellm_provider"],
            "input_usd_per_million": round(input_price * 1_000_000, 10),
            "output_usd_per_million": round(output_price * 1_000_000, 10),
            "reported_max_input_tokens": entry.get("max_input_tokens"),
            "reported_function_calling": entry.get("supports_function_calling"),
            "other_reported_cost_fields": {k: v for k, v in sorted(entry.items())
                                           if "cost" in k and k not in
                                           {"input_cost_per_token", "output_cost_per_token"}},
        })
    now = now or datetime.now(timezone.utc)
    return validate_catalog({
        "schema_version": 1,
        "fetched_at": now.isoformat(timespec="seconds").replace("+00:00", "Z"),
        "price_basis": "community_reported_direct_api_standard_uncached",
        "source": {"url": SOURCE_URL, "sha256": hashlib.sha256(raw).hexdigest()},
        "skipped_unpriced_or_zero_price_entries": skipped,
        "models": rows,
    })


def guard_changes(previous, updated):
    """Keep a questionable feed from silently replacing a usable reference."""
    validate_catalog(previous)
    validate_catalog(updated)
    before = {row["id"]: row for row in previous["models"]}
    after = {row["id"]: row for row in updated["models"]}
    for provider in PROVIDERS:
        old_ids = {key for key, row in before.items() if row["provider"] == provider}
        new_ids = {key for key, row in after.items() if row["provider"] == provider}
        if len(old_ids - new_ids) / len(old_ids) > 0.25:
            raise ValueError(f"More than 25% of {provider} entries disappeared; inspect upstream")
    for model_id in before.keys() & after.keys():
        for field in ("input_usd_per_million", "output_usd_per_million"):
            ratio = after[model_id][field] / before[model_id][field]
            if ratio > 10 or ratio < 0.1:
                raise ValueError(f"Price changed over tenfold for {model_id}; inspect upstream")


def validate_aliases(data):
    aliases = data.get("aliases") if isinstance(data, dict) else None
    if not isinstance(aliases, dict) or not isinstance(data.get("verified_at"), str):
        raise ValueError("Malformed alias map")
    for alias, target in aliases.items():
        if not isinstance(target, str) or not target.strip() or alias in aliases.values():
            raise ValueError(f"Malformed alias: {alias}")
    return data


def rank(data, model_ids, input_tokens, output_tokens, now=None, alias_map=None):
    validate_catalog(data)
    aliases = validate_aliases(alias_map)["aliases"] if alias_map else {}
    if any(not isinstance(n, int) or isinstance(n, bool) or n < 0 for n in (input_tokens, output_tokens)):
        raise ValueError("Token estimates must be nonnegative integers")
    if input_tokens + output_tokens == 0:
        raise ValueError("At least one token estimate must be positive")
    if not model_ids:
        raise ValueError("Supply actual available model IDs")
    now = now or datetime.now(timezone.utc)
    age = (now - parse_time(data["fetched_at"])).total_seconds()
    if age < -300:
        raise ValueError("Catalog timestamp is in the future")
    if age > MAX_AGE_DAYS * 86400:
        raise ValueError(f"Catalog is over {MAX_AGE_DAYS} days old; refresh or use a labeled host-tier fallback")
    stale = age > STALE_AFTER_DAYS * 86400
    by_id = {row["id"]: row for row in data["models"]}
    ranked, unknown = [], []
    for model_id in dict.fromkeys(model_ids):
        # An exact catalog ID always wins; aliases are explicit, never fuzzy.
        resolved = model_id if model_id in by_id else aliases.get(model_id, model_id)
        row = by_id.get(resolved)
        if row is None:
            unknown.append(model_id)
            continue
        ranked.append({
            **row,
            **({"requested_as": model_id, "alias_verified_at": alias_map["verified_at"]}
               if resolved != model_id else {}),
            "estimated_standard_token_cost_usd": round((input_tokens * row["input_usd_per_million"]
                                                        + output_tokens * row["output_usd_per_million"]) / 1e6, 10),
        })
    ranked.sort(key=lambda row: (row["estimated_standard_token_cost_usd"], row["id"]))
    return {
        "status": ("estimated_stale" if stale else "estimated") if ranked else "no_matching_prices",
        "fetched_at": data["fetched_at"],
        "catalog_age_days": round(max(age, 0) / 86400, 1),
        "price_basis": data["price_basis"],
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "ranked": ranked,
        "unpriced_ids": unknown,
        "limitations": "Not a capability test, availability check, subscription quote, or verified cheapest claim. "
                       "Excludes cache/batch/tier/context/tool charges and retry/review overhead; check official pricing.",
    }
