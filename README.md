# Breadth First

A shared skill for **Codex and Claude Code** that deliberately widens coverage
before narrowing to a decision. More reasoning effort alone can deepen familiar
ideas without discovering different ones.

**Lead plans → inexpensive capable workers explore → a stronger model
consolidates → a fresh-context challenger attacks the result → lead decides.**

| Role | Codex family | Claude Code family | Hard cap per run |
| --- | --- | --- | --- |
| Lead | Astra | Fable | 1 |
| Collectors | Luna | Haiku | 100 |
| Consolidators | Sol | Sonnet | 20 |
| Challengers | Sol | Opus | 5, in at most 2 rounds |

The skill names model families, not versions. At each run it uses the newest
selectable version of each family, so a new release needs no change here.

## The workflow

0. **Delegation check.** If one agent could answer with a few searches, it
   answers directly and the skill stops.
1. **Tiers.** Resolve each family to its newest selectable model.
2. **Plan.** 2–3 rounds of three self-directed questions, each round building
   on the last: the field, its sources, then gaps and counterevidence.
3. **Map and size.** Cut the coverage map into packets with distinct angles.
   The packet count picks the size tier:

   | Tier | Collector packets | Consolidators | Challengers | Approval |
   | --- | --- | --- | --- | --- |
   | Small | 3–6 | 1 | 1 per round | none |
   | Medium | 7–15 | 2–4 | 1–2 per round | asked once, after the pilot |
   | Large | 16–100 | 5–20 | 2–3 per round, 5 total | asked once, after the pilot |

4. **Pilot.** 2–3 collectors go first. The lead checks the model (no fallback
   warning), that the evidence file parses, that search returned real pages,
   and that no tool was missing, before scaling.
5. **Collect.** Each collector writes one JSONL file per packet with verbatim
   quotes and returns a short summary.
6. **Spot-check, consolidate, challenge.** Consolidators refetch 2 random
   records per packet and confirm the quote is on the page; failing packets are
   rerun one tier up. Then consolidation, challenge round 1 (objections back to
   the consolidators), revision, and challenge round 2 (decision brief).
7. **Decide.** The lead checks decisive sources and reports with a coverage
   note.

Both hosts are set to manual invocation only (`disable-model-invocation` in
`SKILL.md`, `allow_implicit_invocation: false` in `agents/openai.yaml`), so a
large run is always the user's choice.

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

It is not for quick lookups, questions with one known answer, or deep work on
one chosen option.

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
overwrite existing installations. Keep this checkout in place and run
`git pull --ff-only` to receive instruction updates. If symlinks are unavailable
or your host does not follow them, copy the complete `skills/breadth-first`
directory to the appropriate discovery directory instead. These are filesystem skill packages,
not automatically installed ChatGPT or Claude web-app integrations. A host that
can read files but lacks skill discovery can be asked to read `SKILL.md` directly.

If native delegation, model selection, or browsing is unavailable, the skill
reports that limitation and uses a bounded sequential workflow. It never pretends
that workers ran, that another model was used, or that inaccessible sources were
searched.

## A real run

`/breadth-first How do open-source projects fund their maintainers?`, run on
2026-11-15 under the current rules. Every artifact is in
[`examples/oss-funding/`](examples/oss-funding/): the ledger, one JSONL file
per packet, the spot-check log, both consolidations, the round-1 challenge, the
round-2 brief, and the [lead's answer](examples/oss-funding/answer.md). The
counts below are from those files, not from any agent's summary, and the test
suite checks the example against the record schema.

| Stage | Agents | Result |
| --- | --- | --- |
| Pilot | 2 Haiku (p01, p03) | Files parsed, real pages fetched, no fallback warning, snippet-only 12% and 31% |
| Collect | 2 more Haiku | 60 records, 46 fetched in full |
| Spot-check | 1 Sonnet consolidator | 12 first-pass records: all 12 quotes on the page; after the lead's audit, all 12 claim more than their quote, so every first pass fails |
| Rerun | 4 Sonnet | One rerun per failed packet, one fact per record: 89 records, 82 in full. Spot-check 9 `yes`, 3 `partial`: p01r, p03r, p04r pass; p02r fails, so commercial routes are unranked |
| Consolidate | same Sonnet | Ranked routes on reliability and availability separately |
| Challenge 1 | 1 fresh Opus | Moved employment up on survey data; flagged GitHub Sponsors' concentration; split grants from employment |
| Revise | same Sonnet | Accepted most objections, rejected five with evidence IDs |
| Challenge 2 | 1 fresh Opus | Settled two disputes with 4 fetches, wrote the decision brief |
| Lead check | lead | Found the brief's top claim wrong: donations are 25% of income, salaries 24% |

What the run showed:

- **Quote presence is not enough.** Every sampled quote was real, yet all 12
  sampled first-pass Haiku claims said more than their quotes. That is why the
  spot-check records `supports_claim` and collectors write one fact per record.
  Sonnet reruns told the same rule did better (9 of 12 fully supported) but
  not perfectly: the commercial rerun still failed.
- **The lead check matters.** The only record of the 25% donations figure was
  in a failed, set-aside packet, so both review rounds ranked without it. The
  skill now tells the lead to reread set-aside records for decisive figures and
  log its own checks in `packets/lead.jsonl`.
- **Reviewers misjudge too.** The consolidator marked partial records as
  `yes`. Code review of this example caught two, and the lead's audit of every
  `yes` found four more. The lead's corrected verdict
  goes in `review/lead-spotcheck.jsonl`, never into the reviewer's log, and a
  test now recomputes every packet's pass or fail from the logs and checks the
  ledger against it.
- **Budget.** At 12 searches and 15 fetches, snippet-only records fell from
  48% (previous run, 8 and 8) to 23% of first-pass records.

Lead's ranking, condensed: employment that covers maintenance, then one-off
grants, then donations (open to almost anyone, thin for most). Commercial
routes (selling a licence yourself, pooled subscriptions) are listed but
unranked, because their packet failed twice. Token rewards backfired;
retroactive funding pays in tokens. Not covered: foundation-employed
maintainers and any median payout.

## Evaluating it

[`evals/`](evals/README.md) compares the skill against a single lead at the
same dollar cost on tasks with a published answer key, scoring distinct valid
items, novel finds, duplicate rate and cost over repeated runs. Run it before
tuning caps or tiers.

See [host adapters](skills/breadth-first/references/hosts.md) and
[working templates](skills/breadth-first/references/templates.md) for details.
Licensed under [MIT](LICENSE).
