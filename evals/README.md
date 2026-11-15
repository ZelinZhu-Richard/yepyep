# Evaluating breadth-first

The skill claims that many cheap collectors plus review find more of a field
than one strong agent would at the same cost. This harness tests that claim.
Run it before tuning caps, tiers or prompts, so changes are judged by numbers.

## Design

- **Tasks:** 3–5 questions whose answer set is already published, such as a
  field with a recent survey paper or a curated taxonomy. Build the answer key
  from that source (`tasks.md` explains how). Both arms are told not to use
  that source, and items cited only from it are discarded during grading.
- **Arms:**
  - `breadth`: `/breadth-first <task>` (or `$breadth-first` in Codex), the
    full workflow.
  - `collect-only`: the same collectors and lead, but no spot-check,
    consolidation or challenge; the lead synthesizes straight from the packet
    files. In the demo run, review cost more than ten times the collectors, so
    this arm tests whether review earns that cost.
  - `single`: the same lead model, no subagents, with the prompt in `tasks.md`.
- **Budget matching:** a model cannot see its own spend, so "stop at $X" does
  not hold. Cap `single` mechanically instead:
  - Use the host's own spending or turn limit if it has one.
  - Otherwise cap search and fetch calls. Give `single` the same number of
    search plus fetch calls the `breadth` run made in total (count them from
    the packet budgets used), and say so in its prompt.

  Then compare all arms on the cost each actually used, read from the host's
  usage display afterwards, not on the cap. Record tokens and call counts too.
- **Repeats:** at least 3 runs per task per arm. Single runs are too noisy to
  compare.
- **Grading:** for each run, list every distinct item in the final answer and
  mark it valid or invalid, and which key item it matches (or none). Grade
  blind to the arm: strip model names and coverage notes first. A grader
  from a different model family, or a person, avoids grading its own style.

## Metrics

| Metric | Meaning |
| --- | --- |
| Distinct valid | Unique valid items: matched key items plus novel valid items |
| Key recall | Matched key items / key size (`key_size` in each run file) |
| Invalid listed | Items graded invalid (what review should remove) |
| Novel valid | Valid items not in the key (the niche finds the skill exists for) |
| Duplicate rate | 1 − distinct items / listed items |
| Cost | Dollars from the host's usage display |

`breadth` earns its cost only if distinct valid and novel valid are clearly
higher than `single` across runs, not in one run. Review earns its cost only
if `breadth` beats `collect-only` on valid items or on invalid items removed.

## Recording and scoring

Write one JSON file per run in `runs/` (format in `runs/example.json`), then:

```sh
python3 evals/score.py evals/runs
```

It prints mean and range per task and arm. The example file is ignored.
A full pass (3 tasks, 3 arms, 3 runs) is 27 runs; start with one task to
check the grading before running the rest.
