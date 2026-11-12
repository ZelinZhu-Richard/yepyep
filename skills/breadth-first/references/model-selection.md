# Model selection

1. Discover actual native subagent capabilities and the host's model menu. Record
   source/time, selectable IDs, tool access, context limits, and concurrency.
2. Determine how usage is charged. Prefer host/account-specific prices and limits.
   Public API prices do not establish Codex or Claude subscription cost.
3. Consult the bundled catalog only as a secondary estimate of direct-provider
   API token prices. Its source is LiteLLM's community-maintained public catalog;
   `fetched_at` is retrieval time, not provider verification time. Prices, supported
   model names, capability flags, and billing tiers may be incomplete or wrong.
4. Check official pricing when accessible: https://openai.com/api/pricing/ and
   https://platform.claude.com/docs/en/about-claude/pricing . Resolve ambiguity in
   favor of account-specific information, not a lower unverified estimate.
5. Match exact IDs. Never guess that a host alias, “mini,” “Luna,” or “Haiku” maps to
   a particular priced API model. The only aliases resolved are the ones listed in
   `host-aliases.json` (Claude Code's `haiku`, `sonnet`, `opus`, `fable`). That file
   is maintained by hand; the output shows `requested_as` and `alias_verified_at`
   so a mapping that predates a model release is visible. Anything else stays
   unpriced.
6. Filter for task suitability first: source access, tool use, language, context,
   extraction reliability, and required verification. A low price does not show
   suitability. Use a small representative packet to assess reliability when
   uncertainty matters; the packet counts toward the budget and real research.
7. Compare expected input and output use, plus retries, review overhead, and tool
   fees. Escalate a packet when cheap output is unreliable instead of repeatedly
   retrying the same failing strategy.

The stdlib helper ranks only IDs supplied by the caller, never the entire feed:

```sh
python3 scripts/rank_models.py --model AVAILABLE_ID_OR_ALIAS --model ANOTHER \
  --input-tokens 60000 --output-tokens 3000
```

Estimate tokens for one packet, not one message. A search worker's input is
mostly fetched pages and accumulates across tool calls, so input price usually
decides the ordering; a reviewer reading many evidence files is similar.

Run that command from this skill's directory. Its estimate is
`input_tokens * input_USD_per_million / 1e6 + output_tokens * output_USD_per_million / 1e6`.
It uses standard uncached prices. Cache, batch, reasoning-token, long-context,
regional, service-tier, and tool charges may change the ordering. Conditional
pricing fields are preserved for inspection, not silently applied. The output
labels unknown IDs and estimated prices. Data older than seven days is still
ranked but marked `estimated_stale` with `catalog_age_days`; say so when citing
it. Data older than 30 days, future timestamps, and malformed catalogs are
rejected with a nonzero exit status.

Do not interpret missing prices as zero. If prices cannot be compared, say
“lowest-cost tier indicated by the host” or “user-preferred worker; cost unverified,”
not “verified cheapest.” A failed refresh must not re-date old data as fresh.

The role preferences in `SKILL.md` are the default assignment. The price check
exists to catch the case where a cheaper selectable model is also capable, and
to show the user what the run is expected to cost. A catalog entry does not
prove the host can select that model; the host's own model ID may also differ
from the API ID. The main model is selected by the user/host; this skill cannot
upgrade a running lead agent.
