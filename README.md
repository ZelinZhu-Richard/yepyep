# Breadth First

A shared skill for **Codex and Claude Code** that deliberately widens coverage
before narrowing to a decision. More reasoning effort alone can deepen familiar
ideas without discovering different ones.

**Lead plans → inexpensive capable workers explore → a stronger model
consolidates → a fresh-context challenger attacks the result → lead decides.**

| Role | Codex family | Claude Code family | Hard cap per run | Typical |
| --- | --- | --- | --- | --- |
| Lead | Astra | Fable | 1 | 1 |
| Collectors | Luna | Haiku | 100 | 20–30 |
| Consolidators | Sol | Sonnet | 20 | 5–10 |
| Challengers | Sol | Opus | 5, in at most 2 rounds | 2–3 |

The skill names model families, not versions. At each run it uses the newest
selectable version of each family, so a new release needs no change here.

## The workflow

1. First ask: **What is the cheapest capable subagent model actually available in
   this session?** The collector family is the standing answer; the lead
   resolves every family to its newest selectable version.
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
5. Consolidators deduplicate, assess evidence, and explain exclusions.
   Challengers get two rounds and no more: round 1 sends objections back to the
   consolidators, who revise; round 2 writes the decision brief for the lead.
6. The lead checks decisive evidence, fills important gaps within budget, and
   delivers the answer and recommendation with coverage limits. It does not pause
   for approval before dispatch.

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

See [host adapters](skills/breadth-first/references/hosts.md) and
[working templates](skills/breadth-first/references/templates.md) for details.
