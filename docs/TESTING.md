# Automated checks

Run the current suite from the repository root with Python 3.12 or newer and Git installed:

```sh
python -m unittest discover -s tests -v
```

No Python packages need to be installed. Python is used only for repository checks; this does not select a language or engine for the game.

## Current coverage

- Inline Markdown links and images point to tracked files with correct case. Links to Markdown headings resolve. Code-fenced examples and external URLs are excluded.
- The current Markdown issue templates have nonempty name/about metadata and unique names.

The checker handles the inline link syntax currently used in this repository, not every Markdown extension. If adding a new link format or YAML issue forms, extend the checks appropriately. It does not check external website availability or prove that documentation is accurate. Stage new link targets before running locally, so the Git index includes them.

## Pull requests

The `PR checks` GitHub Actions workflow runs the suite on PR creation, updates, and reopening, as well as pushes. Its check is named **Repository checks**. There are no path filters, so documentation-only PRs run it too. It uses a read-only token, no repository secrets, and no write credentials for checkout. Fork contributions use the normal `pull_request` event; a maintainer may need to approve a first-time contributor's workflow run in GitHub.

To block merging when tests fail, a maintainer must enable **Require status checks to pass before merging** for `main` and select **Repository checks** after the check has run. Workflow files alone do not enforce merge protection. If using rulesets, choose GitHub Actions as the expected source when available. If a maintainer has permission to bypass the applicable protection, the check can also be bypassed; keep a separate required-check rule without bypass if passing tests must be mandatory for everyone.

If a merge queue is adopted later, add its `merge_group` trigger. Do not disable the workflow or remove checks just to make a failing PR mergeable; diagnose the failure and update tests alongside intentional behavior changes.

## Game tests after engine selection

No game code or playable build exists yet. This suite does not test movement, room boundaries, NPC interaction, or gameplay. Once the engine is agreed and implementation exists, add its actual automated tests to CI. The first useful coverage should include boundaries, opening/closing dialogue, and restoring movement. Record manual playtest results separately; passing CI does not replace playtesting.
