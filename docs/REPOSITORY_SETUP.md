# Repository setup and inviting contributors

Repository: [Meeka89/HUAIC-Game-Project](https://github.com/Meeka89/HUAIC-Game-Project). The initial documentation setup does not create live issues or configure GitHub settings, contributor permissions, or branch protection.

## Maintainer next steps

1. Review the kickoff materials and initial tasks. Keep private content out of public records; repository licensing and contributor ownership questions remain unresolved in [ASSETS_AND_CREDITS.md](ASSETS_AND_CREDITS.md).
2. For future changes, follow [CONTRIBUTING.md](../CONTRIBUTING.md): review `git status` and the diff, commit focused work on a branch, and submit a PR for review.
3. To use another computer, clone `https://github.com/Meeka89/HUAIC-Game-Project.git`. Inspect `git remote -v` before publishing changes and preserve the existing remote unless a change is agreed.
4. Replace remaining README and communication TBDs with confirmed details. Invite Joe and participating members with appropriate access; no account is required just to contribute ideas through the chosen communication channel.
5. Review [INITIAL_TASKS.md](INITIAL_TASKS.md), create only the agreed live issues, and let people claim small tasks. Keep owners and target dates unassigned until accepted.

## Recommended GitHub settings — not configured

- Use reviewed pull requests into `main`, avoiding direct pushes where feasible. Consider a rule requiring review before merging once repository access and the review workflow are ready.
- Tag issues by contribution type (for example, code, design, writing, art, music, docs, research, playtesting) and difficulty (small, medium, larger).
- Rule availability and enforcement depend on repository configuration, visibility, and GitHub plan. Verify what is available before claiming protection is enabled.

The repository now includes a small automated PR test suite at Micah's request. Enable **Require status checks to pass before merging** for `main` and select **Repository checks** once it has run; see [TESTING.md](TESTING.md). This documentation does not claim that setting is configured. Bots, automated game builds, and Discord integrations can wait until the team has an agreed need.
