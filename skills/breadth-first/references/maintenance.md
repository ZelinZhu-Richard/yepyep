# Maintenance and freshness

The GitHub Actions workflow runs every Monday at 13:00 UTC (08:00 New York in
standard time, 09:00 in daylight time) and can be run manually. Schedules are
best-effort; GitHub can delay them and can disable schedules on inactive public
repositories. The workflow must exist on the default branch and Actions must be
enabled. It needs `contents: write` to commit the generated reference file.
Branch protection or organization policies may prevent that write; a failed run
leaves the prior data unchanged and is visible in Actions.

The updater downloads LiteLLM's public catalog over verified HTTPS, extracts
direct OpenAI/Anthropic chat entries with valid positive standard token prices,
retains conditional price metadata, records a SHA-256 and retrieval timestamp,
and atomically replaces `model-catalog.json` only after validation. Unexpected
schema/price changes and suspiciously large model removals fail closed. No API
keys or paid inference are needed. Community reports are estimates, not official
provider verification. Changing vendor pricing sources requires a code change.

The automation updates **model reference data**, not the skill's behavior or
model role preferences. At each invocation the lead still verifies availability,
capabilities, billing basis, and freshness. A fresh download does not prove the
upstream price was recently verified. The example GPT-6 host names remain unpriced
if the source has no exact match.

From the repository root:

```sh
python3 skills/breadth-first/scripts/refresh_models.py
python3 -m unittest discover -s tests -v
```

The refresh exits nonzero on failure and leaves the previous catalog intact. Do
not disable TLS verification to get an update through. Inspect source changes
when validation fails instead of weakening the validator to accept bad data.

GitHub updates the repository; it cannot update an arbitrary local checkout.
For an installed symlink, run `git pull --ff-only` in this repository when it has
no conflicting local changes. A copied installation needs to be copied again.
The skill's invocation-time freshness check catches installations left stale.
`refresh_models.py` may be run from an installed copy to refresh just its own
catalog when network access and write permissions allow it. Record that as a
local refresh, not a GitHub publication.
