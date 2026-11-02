# Contributing

All experience levels and contribution types are welcome. Check existing GitHub issues and [draft planning tasks](docs/INITIAL_TASKS.md) before starting so work is not duplicated. An **issue** is a shared description of a task, idea, or bug; it is not automatically an approved requirement. Larger features need agreement before implementation.

## A small shared workflow

1. **Propose or choose a task.** Describe the context, scope, dependencies, and an observable way to tell it is complete. Ideas remain proposals until reviewed.
2. **Claim it.** Comment on the issue and confirm an owner so others know who is working on it. Choose a realistic target date together if useful; do not assign someone without their agreement.
3. **Create a branch.** A branch is a separate line of work that lets you edit without changing the shared `main` branch. Use a short name such as `docs/kickoff-notes` or `task/short-description`.
4. **Implement.** Make a focused change. A **commit** is a named snapshot of your changes; use a brief message explaining what changed.
5. **Verify.** Read and check documentation, inspect asset permissions, or use the project's agreed code checks and playtests once available. Record what you actually checked and anything you could not check.
6. **Open a pull request (PR).** A PR asks to bring your branch into `main`. Link the issue and explain the change and verification using the PR template.
7. **Review.** Another person reads or tries the change and asks questions or requests fixes. Initially Micah Kelley and Joe Faith review merges; agreed future maintainers can share this responsibility.
8. **Merge.** After review and any fixes, a maintainer combines the branch into `main` and closes the completed issue. Avoid direct pushes to `main` where feasible.

Repository: [Meeka89/HUAIC-Game-Project](https://github.com/Meeka89/HUAIC-Game-Project). Once Git is installed, download a working copy with `git clone https://github.com/Meeka89/HUAIC-Game-Project.git`, then open the resulting `HUAIC-Game-Project` folder. Engine/setup/run instructions: **pending engine selection**. Do not guess commands for a game that has not been chosen.

## Contributing without Git

You can pitch an idea, write text, sketch art, research a question, or test a build without learning Git immediately. Discuss the task and how to submit it with a maintainer. Discord is proposed, pending confirmation; email/contact details are TBD. Maintainers can help turn work received through Discord into an issue or PR, credit the contributor, and confirm the proposed edit with them. Do not post private information or assets without permission.

Planning at kickoff needs neither a GitHub account nor development tools. Volunteers can take small, temporary responsibilities; permanent departments are not required. Participation is flexible, and asking for help or handing off a task is welcome.

## Example sizes

- **Small:** clarify a paragraph, research one engine constraint, or report a reproducible bug once a build exists.
- **Medium:** compare a few suitable engines after narrowing the concept, or create one agreed asset with documented permission.
- **Larger:** implement an agreed core mechanic after concept and engine selection. Discuss it first and split it into smaller, reviewable tasks.

AI-assisted work is welcome. Read [AGENTS.md](AGENTS.md), give your tool shared project context, explain the submitted changes yourself, and help verify them. Keep private chats out of submissions. Record asset sources and permissions in [assets and credits](docs/ASSETS_AND_CREDITS.md); repository licensing and contributor ownership terms remain unresolved.
