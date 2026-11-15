# Eval tasks

Pick 3–5 tasks. For each, record the key source and the key in `keys/<task>.md`.

## Choosing a task

A good task:

- asks for a whole field ("all the ways", "every approach"), not one answer;
- has a published, citable answer set: a survey paper, a standards body's
  taxonomy, or a well-maintained curated list;
- has items that are discussed outside that source, so a scan can find them
  independently;
- mixes mainstream items with a long tail of niche ones.

Example shapes (choose the actual key source yourself and check it exists):

| Task id | Question | Key source type |
| --- | --- | --- |
| oss-funding | How do open-source projects fund their maintainers? | Survey or foundation report on OSS sustainability |
| llm-halluc | What methods exist to detect hallucinations in LLM output? | Recent survey paper on hallucination detection |
| solo-income | What are the ways a solo software developer earns income? | Industry survey of indie developers |
| study-methods | Which evidence-based study techniques exist for exam preparation? | Review article on learning techniques |

## Building the key

1. Take every distinct item the source lists. Merge synonyms into one key item
   with an id (`k01`, `k02`, ...).
2. Note which items are niche: mentioned by the source but rarely elsewhere.
3. Freeze the key before running either arm.

## Prompts

`breadth` arm:

```text
/breadth-first <question>. Do not use <key source> or pages that copy it.
Run without asking for approval.
```

`single` arm (same lead model, no subagents):

```text
<question>. Search widely and list every distinct approach you can support with
a source, including niche ones. Do not use <key source> or pages that copy it.
Do not use subagents. Stop when you have spent about $<breadth cost>.
```
