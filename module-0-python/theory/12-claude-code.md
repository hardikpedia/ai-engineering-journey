# 0.12 AI-assisted dev with Claude Code

[← 0.11 FastAPI](11-fastapi.md) · [Module 0](../README.md) · Next: [Project →](../project/README.md)

**Use a coding agent for leverage, verify everything it writes. AI multiplies your fundamentals; it doesn't replace them.** That's why this unit comes last: learn Python yourself first, then speed up.

## Install (from the official docs)

```bash
# macOS / Linux / WSL
curl -fsSL https://claude.ai/install.sh | bash
# Windows PowerShell
irm https://claude.ai/install.ps1 | iex

cd project && claude        # log in on first run
```

## The building blocks

| Feature | What it is | Use it for |
| --- | --- | --- |
| `CLAUDE.md` | Markdown file in the repo root, read at the start of every session | Stack, commands, conventions ("run `uv run pytest` before finishing") |
| Skills | Packaged, reusable workflows you trigger by name | `/review-pr`, "write tests for this module" |
| Subagents | Separate agents that work on parts of a task in parallel | A reviewer, a tester, a researcher |
| Hooks | Shell commands that run before/after agent actions | Auto-format after every edit, run tests before a commit |
| MCP | Open standard for connecting external tools and data | Jira, Google Drive, databases (you build one in Module 5) |

## The verification loop — use it on every change

1. Give context and a clear spec (what, constraints, how to test).
2. Ask for a plan first; review it before any code is written.
3. Let it implement.
4. Read the full diff yourself.
5. Run tests and try the feature by hand.
6. Accept, or explain what's wrong and repeat.

**Vibe coding** = accepting whatever comes out. **AI-assisted engineering** = directing and verifying. Interviewers can tell the difference within two follow-up questions.

## Do (after your project passes all tests on your own)

- [ ] Write a `CLAUDE.md` for the project: stack, folder layout, commands, rules.
- [ ] Ask Claude Code to add `?units=fahrenheit` to `/brief` with a test. Plan first, review the diff.
- [ ] Add one hook (e.g. run `uv run pytest -q` after edits).
- [ ] Write down one mistake the agent made: what it proposed, why it was wrong, how you caught it, what you changed.

Docs: [Claude Code overview](https://code.claude.com/docs/en/overview)
