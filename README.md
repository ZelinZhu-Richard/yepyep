# Breadth First

A shared skill for **Codex and Claude Code** that deliberately widens coverage
before narrowing to a decision. More reasoning effort alone can deepen familiar
ideas without discovering different ones.

**Lead plans → inexpensive capable workers explore → a stronger model
consolidates → a fresh-context challenger attacks the result → lead decides.**

| Role | Codex | Claude Code |
| --- | --- | --- |
| Lead | GPT-6 Astra | Fable or Opus |
| Collectors | GPT-6 Luna | Haiku |
| Consolidator and challenger | GPT-6.1 Sol | Opus under a Fable lead, Sonnet under an Opus lead |

## The workflow

1. First ask: **What is the cheapest capable subagent model actually available in
   this session?** Check runtime capabilities, billing, and price freshness.
2. Use 2–3 planning rounds of three self-directed questions each. Every round's
   questions build on the previous round's answers: the field, then its sources,
   then the gaps and counterevidence.
3. Build a coverage map and divide it into bounded assignments. The lead chooses
   how many workers each area needs **after decomposition**. There is no fixed
   number per platform, and simple tasks need not spawn workers.
4. Assign distinct retrieval/extraction tasks to inexpensive workers, each with
   its own angle and seed queries. Workers write evidence to files and return
   short summaries, so the lead's context stays small. Queue work in waves when
   the host limits concurrency.
5. A stronger consolidator deduplicates, assesses evidence, and explains
   exclusions. A challenger then tries to break the shortlist and rescue niche
   findings that were cut for being unusual rather than unsupported.
6. The lead checks decisive evidence, fills important gaps within budget, and
   delivers the answer and recommendation with coverage limits.

The roles are preferences, used when the runtime can select those models. The
skill cannot change the active lead model, so select your lead in the host
before invoking it.

## Use it

This repository contains one canonical skill:
[`skills/breadth-first/SKILL.md`](skills/breadth-first/SKILL.md).
Both discovery directories link to it, so they cannot drift apart:

```text
.agents/skills/breadth-first -> ../../skills/breadth-first  # Codex
.claude/skills/breadth-first -> ../../skills/breadth-first  # Claude Code
```

Open this repository in the host and reload/start a session if needed:

```text
Codex:       $breadth-first Map practical ways to earn income, including niche approaches.
Claude Code: /breadth-first Map practical ways to earn income, including niche approaches.
```

For another project, run from this repository (Python 3.10+; no dependencies):

```sh
python3 scripts/install.py --project /path/to/project --host both
```

Or install for your user:

```sh
python3 scripts/install.py --personal --host both
```

Choose `--host codex` or `--host claude` to install only one adapter. The installer
creates symlinks on systems that support them, is repeatable, and refuses to
overwrite existing installations. Keep this checkout in place. If symlinks are
unavailable or your host does not follow them, copy the complete
`skills/breadth-first` directory to the appropriate discovery directory instead;
refresh copied installations separately. These are filesystem skill packages,
not automatically installed ChatGPT or Claude web-app integrations. A host that
can read files but lacks skill discovery can be asked to read `SKILL.md` directly.

If native delegation, model selection, or browsing is unavailable, the skill
reports that limitation and uses a bounded sequential workflow. It never pretends
that workers ran, that another model was used, or that inaccessible sources were
searched.

## Weekly model reference updates

[`refresh-models.yml`](.github/workflows/refresh-models.yml) runs every Monday at
13:00 UTC and supports **Run workflow** in GitHub Actions. It validates the updater,
downloads the public pricing feed, validates the result, and commits only
`skills/breadth-first/references/model-catalog.json` to the default branch.
The workflow does not rewrite behavioral instructions or execute paid model calls.

Requirements: GitHub Actions enabled, the workflow on the default branch, and
permission for its `GITHUB_TOKEN` to write repository contents. Repository rules
or organization policy can restrict that permission. Schedules are best-effort
and may be disabled after public-repository inactivity. Check the Actions tab for
failures; installation-time validation is not proof of a completed scheduled run.

The source is [LiteLLM's community-maintained model catalog](https://github.com/BerriAI/litellm/blob/main/model_prices_and_context_window.json).
The reference contains direct OpenAI/Anthropic chat API token-price **estimates**,
retrieval time, source URL, and a SHA-256 digest. It is not an official price quote,
a native subagent model menu, or a subscription-cost table. Retrieval time does
not establish when the upstream prices were verified. The helper labels data
older than seven days as stale, refuses it after 30 days, and never treats
missing prices as zero. Claude Code aliases (`haiku`, `sonnet`, `opus`, `fable`)
resolve through the hand-maintained `references/host-aliases.json`, which the
weekly job does not update.

Weekly changes reach GitHub, not arbitrary local copies. Run `git pull --ff-only`
in your clean skill checkout to receive them; linked installations then use the
updated reference. Invocation-time freshness checks detect missed updates.

Manual refresh and checks:

```sh
python3 skills/breadth-first/scripts/refresh_models.py
python3 -m unittest discover -s tests -v
python3 skills/breadth-first/scripts/rank_models.py \
  --model gpt-6-luna --model haiku --input-tokens 60000 --output-tokens 3000
```

The ranking command exits with status 2 for expired/malformed data or when none of
the supplied IDs have prices. Unknown models remain explicit even when other
candidates can be ranked. Failed refreshes preserve the prior catalog.

## Example: map ways to earn income

The lead identifies categories such as employment, services, products, operating
businesses, licensing, and investing, then decides where evidence can be found.
RedNote, Instagram, Reddit, Quora, and Hacker News are possible sources, not a
mandatory list or a complete map of the field. Workers may divide a large source
by community, category, or evidence type. Other sources may need no worker.

The review distinguishes reported revenue from profit, looks for failures and
survivorship bias, and preserves useful niche approaches. Multiple posts repeating
one success story count as one underlying source, not independent confirmation.
The final answer describes covered areas and gaps rather than claiming to have
found every possible way to make money.

See [host adapters](skills/breadth-first/references/hosts.md),
[working templates](skills/breadth-first/references/templates.md), and
[maintenance](skills/breadth-first/references/maintenance.md) for details.
