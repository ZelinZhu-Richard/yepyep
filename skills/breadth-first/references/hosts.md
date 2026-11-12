# Host adapters

The workflow is shared; orchestration depends on the tools the current session
actually exposes. Read their live schemas before calling them. Do not install a
second agent framework or call paid external APIs as a fallback.

## Codex

- Discovery: `.agents/skills/breadth-first/` in a project (scanned from the
  working directory up to the repository root) or `$HOME/.agents/skills/` for a
  personal installation. Symlinked skill folders are followed.
- Invoke with `$breadth-first` and the task.
- Roles: lead GPT-6 Astra, collectors GPT-6 Luna, consolidator and challenger
  GPT-6.1 Sol. Apply them only when the session can select those models.
- A subagent's model is resolved from an explicit value in the spawn request,
  then `agents.default_subagent_model`, then the parent's model. Pass the model
  explicitly for every worker; otherwise collectors silently inherit the
  expensive lead.
- `agents.max_concurrent_threads_per_session` caps open subagent threads. Read
  the limit from the tool or config instead of assuming one, and run in waves.
- Spawn/wait tool names and parameters vary by Codex version. Use the schemas
  exposed in the session; do not invent parameters. Where a model override
  requires a fresh-context child, the brief must carry everything.
- If only one model is selectable, say so and run the workflow on it within the
  budget. Claim no savings from a switch that did not happen.
- Research workers do not edit tracked source files. Do not create a Git
  worktree unless the user asks.

## Claude Code

- Discovery: `.claude/skills/breadth-first/` in a project or
  `~/.claude/skills/breadth-first/` for a personal installation.
- Invoke with `/breadth-first` and the task, or ask Claude to use the skill.
- Keep the orchestrator in the main conversation; this skill deliberately has no
  `context: fork`.
- Roles: the lead is the session model, Fable or Opus. Collectors run on
  `haiku`. Consolidator and challenger run one tier below the lead: `opus` when
  the lead is Fable, `sonnet` when the lead is Opus.
- **Always pass `model` on every Agent call.** With `model` omitted the host
  chooses, and that choice is often not the cheap tier.
- **Do not use the Explore agent type as the cheap collector.** It runs on the
  main conversation's model (Opus under a Fable lead) and cannot write files.
  Use a general-purpose agent with `model: haiku`, which has web search, fetch,
  and file writing.
- The Agent tool accepts the aliases `haiku`, `sonnet`, `opus`, `fable`, and on
  some surfaces full model IDs. `rank_models.py` resolves the aliases through
  `references/host-aliases.json`; that mapping is maintained by hand and shows
  its verification date in the output.
- Default concurrency is 20 running subagents per session
  (`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`); a spawn beyond it fails rather than
  queues. Run waves below the limit and leave slots for reviewers.
- Subagents can spawn their own subagents by default. The worker and reviewer
  briefs forbid it so that only the lead allocates work and budget.
- A subagent may lack tools the lead has, such as MCP connectors. State the
  tools each packet needs in its brief and check the first wave's reports.

## Fallback on either host

If subagents are unavailable, keep the coverage map and run the packets
sequentially in the current agent. Say that no separate workers or second model
were used; another pass by the same model is not independent evidence. If
browsing is absent, use user-provided or connected sources and list the areas
that could not be reached. Never invent results to simulate a scan.

Reference documentation (verified 2026-11-12; check the installed host):
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/sub-agents
