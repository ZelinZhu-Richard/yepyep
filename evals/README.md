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
  - `breadth`: `/breadth-first <task>` (or `$breadth-first` in Codex).
  - `single`: the same lead model, no subagents, with the prompt in
    `tasks.md` and the same cost budget.
- **Budget matching:** match on dollars, not tokens, because the tiers have
  different prices. Run `breadth` first, read its cost from the host's usage
  display, and give `single` that budget. Record tokens too.
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
| Key recall | Matched key items / key size |
| Novel valid | Valid items not in the key (the niche finds the skill exists for) |
| Duplicate rate | 1 − distinct items / listed items |
| Cost | Dollars from the host's usage display |

`breadth` earns its cost only if distinct valid and novel valid are clearly
higher than `single` across runs, not in one run.

## Recording and scoring

Write one JSON file per run in `runs/` (format in `runs/example.json`), then:

```sh
python3 evals/score.py evals/runs
```

It prints mean and range per task and arm. The example file is ignored.
A full pass (5 tasks, 2 arms, 3 runs) is 30 runs; start with 3 tasks.
