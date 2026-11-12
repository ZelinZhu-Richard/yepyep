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
5. Match exact IDs. Never assume a host alias, “mini,” “Luna,” or “Haiku” maps to a
   particular priced API model. A documented host mapping may establish a match;
   otherwise its numeric cost remains unknown.
6. Filter for task suitability first: source access, tool use, language, context,
   extraction reliability, and required verification. A low price does not show
   suitability. Use a small representative packet to assess reliability when
   uncertainty matters; the packet counts toward the budget and real research.
7. Compare expected input and output use, plus retries, review overhead, and tool
   fees. Escalate a packet when cheap output is unreliable instead of repeatedly
   retrying the same failing strategy.

The stdlib helper ranks only IDs supplied by the caller, never the entire feed:

```sh
python3 scripts/rank_models.py --model EXACT_AVAILABLE_ID --model ANOTHER_AVAILABLE_ID \
  --input-tokens 4000 --output-tokens 1000
```

Run that command from this skill's directory. Its estimate is
`input_tokens * input_USD_per_million / 1e6 + output_tokens * output_USD_per_million / 1e6`.
It uses standard uncached prices. Cache, batch, reasoning-token, long-context,
regional, service-tier, and tool charges may change the ordering. Conditional
pricing fields are preserved for inspection, not silently applied. The output
labels unknown IDs and estimated prices, and rejects stale data (over seven days),
future timestamps, and malformed catalogs with a nonzero exit status.

Do not interpret missing prices as zero. If prices cannot be compared, say
“lowest-cost tier indicated by the host” or “user-preferred worker; cost unverified,”
not “verified cheapest.” A failed refresh must not re-date old data as fresh.

The user's Codex role preferences are gpt-6-astra / gpt-6-luna / gpt-6.1-sol.
They are not fabricated entries in the price catalog. The main model is selected
by the user/host; this skill cannot promise to upgrade a running lead agent.
