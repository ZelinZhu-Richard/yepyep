# Host adapters

The workflow is shared; orchestration depends on tools actually exposed in the
current session. Read their live schemas before calling them. These adapters do
not install a second agent framework or use paid external APIs as a fallback.

## Codex

- Discovery location: `.agents/skills/breadth-first/SKILL.md` in a project, or
  `~/.agents/skills/breadth-first/SKILL.md` for a personal installation.
- Invoke with `$breadth-first` and the task. A host without a skill picker can
  explicitly read `skills/breadth-first/SKILL.md`.
- When native collaboration tools are exposed, inspect their model IDs and slot
  limit. In environments with `spawn_agent`, `send_message`, and `wait_agent`,
  use those tools according to their schemas, and retain returned task IDs.
- Some hosts allow model overrides only with fresh-context children (for example,
  `fork_turns: "none"`). Then give each child a self-contained brief with every
  necessary constraint, source, artifact path, and return format. Do not assume
  it inherited the conversation. Do not invent parameters on another host.
- Apply the user's Astra/Luna/Sol preference only to selectable models. If the
  session exposes only one model, say so and use that model within the budget.
  Do not claim savings from switching when no switch occurred.
- Follow repository instructions; use the existing checkout. Do not create a Git
  worktree unless the user explicitly asks. Research workers should not edit
  shared source files; give any necessary output files distinct task paths.

## Claude Code

- Discovery location: `.claude/skills/breadth-first/SKILL.md` in a project, or
  `~/.claude/skills/breadth-first/SKILL.md` for a personal installation.
- Invoke with `/breadth-first` and the task, or explicitly ask Claude to use it.
- Keep the orchestrator in the main conversation. This skill intentionally has
  no `context: fork` setting: a nested agent may lack further delegation tools.
- Inspect the native Agent/Task tool and allowed models. Where exposed, `haiku`,
  `sonnet`, and `opus` are candidate inexpensive-worker, reviewer, and lead roles,
  respectively, not permanent rankings or promises of availability. Resolve
  aliases using host documentation before joining them to API price entries.
- Select model and agent type only through supported fields. Do not assume
  Claude Code exposes a Codex model or that a tool-enabled subagent has access
  to every tool available to the lead. Supply self-contained briefs.
- Respect runtime concurrency and subscription limits. If model selection or
  delegation is disabled, continue with an explicitly labeled fallback.

## Fallback on either host

If subagents are unavailable, preserve the coverage map and run bounded packets
sequentially in the current agent. State that no independent workers or secondary
model were used. A different pass of the same model is not independent evidence.
If browsing is absent, use available user-provided or connected sources and label
the inaccessible areas. Never invent research results to simulate a full scan.

Reference documentation (check current behavior in the installed host):
- https://developers.openai.com/codex/skills/
- https://developers.openai.com/codex/multi-agent/
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/sub-agents
