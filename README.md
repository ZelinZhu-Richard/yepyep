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
2026-11-15. Full artifacts are in [`examples/oss-funding/`](examples/oss-funding/):
the ledger, the four JSONL evidence files, the spot-check log, both
consolidations, both challenges, and the [lead's answer](examples/oss-funding/answer.md).

| Stage | Agents | Result |
| --- | --- | --- |
| Pilot | 2 Haiku (p01, p03) | Files parsed, real pages fetched, no fallback warning |
| Collect | 2 more Haiku | 46 records, 29 fetched in full, all four packets hit their search budget |
| Spot-check | 1 Sonnet | 8 of 8 quotes found on the live page; 2 were stitched from separate sentences |
| Consolidate | same Sonnet | Ranked routes by reliability; flagged self-reported figures |
| Challenge 1 | 1 Opus | Tidelift had been acquired; employer pay rested on one person; Sovereign Tech had grown past a pilot |
| Revise | same Sonnet | Accepted two objections, rejected one with reasons |
| Challenge 2 | 1 Opus | Fetched two sources, found Tidelift still paying, wrote the brief |

Tokens by tier: Haiku about 413k, Sonnet about 198k, Opus about 207k, plus the
lead. At list prices the Sonnet and Opus review cost more than ten times the
four collectors combined (search fees aside), which is why the caps on those
tiers matter most.

Lead's ranking, condensed: employer-paid maintenance, then public fellowships
(very few places), then selling a paid extension or licence yourself, then
sponsorships and sponsorware (open to anyone, usually small). Fiscal hosts route
money but are not a source; bounties and token rewards are unreliable. The
answer lists grants, median income data and country eligibility as uncovered.

What the run changed in the skill: the stitched quotes led to the
"one contiguous span" rule and the `stitched` spot-check result.

## Evaluating it

[`evals/`](evals/README.md) compares the skill against a single lead at the
same dollar cost on tasks with a published answer key, scoring distinct valid
items, novel finds, duplicate rate and cost over repeated runs. Run it before
tuning caps or tiers.

See [host adapters](skills/breadth-first/references/hosts.md) and
[working templates](skills/breadth-first/references/templates.md) for details.
Licensed under [MIT](LICENSE).
