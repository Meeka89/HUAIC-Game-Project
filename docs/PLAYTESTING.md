# Playtesting

No game, build, engine, or setup/run instructions exist yet. Once an engine is selected, document how developers run the current source. Nontechnical testers should receive a packaged playable build and short launch/control instructions rather than needing development tools.

Initially, maintainers will export builds manually and publish them through GitHub Releases once builds exist. Each release should identify its build version and exact source commit, with platform and launch instructions. Review included files and asset permissions before distribution.

A build is a **snapshot of a particular commit**. It does not automatically update when `main` changes. Testers should download a newer release when asked and report the version they actually tested.

## Useful feedback

Use the bug report template for problems and include:

- Build version/release and, if known, source commit; operating system/platform.
- Steps that someone else can follow to reproduce the problem.
- Expected result and actual result; how often it happens.
- Useful screenshots or logs with private information removed.

For general feedback, describe what you tried, what felt enjoyable or confusing, and one concrete improvement suggestion. Suggestions are proposals, not automatically planned features. Maintainers review reports and turn agreed fixes into small tasks.

Browser builds and automated builds are future possibilities depending on engine choice and actual needs. Neither is configured or promised.
