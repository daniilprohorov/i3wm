---
name: commit
description: Create a concise commit message and run only git commit -m when the user asks to commit.
---

# Commit Skill

Use this skill when the user asks to commit changes and wants only commit message creation plus commit execution.

## Scope

This skill has a single responsibility:

1. Propose a concise, action-oriented commit message.
2. Execute commit using exactly one command.

## Allowed Command

The only command this skill is allowed to execute is:

```bash
git commit -m "<message>"
```

No other shell commands are allowed within this skill.

## Model Requirement

- Use the `gpt-5.4-mini` model for this skill.

## Message Rules

- Prefer imperative style, short and clear.
- Avoid trailing punctuation.
- Reflect the actual change scope provided by the user.
