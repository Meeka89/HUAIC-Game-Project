# Confirmed decisions and constraints

The following are confirmed by Micah Kelley's supplied project brief. They are not claims of a kickoff vote or later meeting approval.

| Topic | Confirmed direction |
| --- | --- |
| Priorities | Learn effective AI use first, collaboration second, and finish a small enjoyable game third. |
| Initial scope | Small single-player game. Multiplayer is outside the initial scope. |
| Target | Early May 2027 is a target, not a guaranteed release date. |
| Participation | About 10 people with mixed experience; flexible participation, approximately 1–2 meetings per month, and optional work between meetings. Noncoding contributions are welcome. |
| Initial maintenance | Micah Kelley, club president, and Joe Faith, faculty advisor, initially maintain and review merges. Student ownership and shared maintenance should grow over time. |
| Kickoff | The first half of the hour is a separate ChatGPT study-workspace workshop; the second half is repository introduction and game planning. Micah operates the repository from his laptop; participants need no accounts or development tools for planning. |
| Next-meeting goal | A reviewed game plan, not necessarily a playable prototype. |
| Shared record | GitHub is the official source for agreed plans, decisions, tasks, and changes. Discussion alone is not approval. |
| AI meeting support | Recording requires participants' knowledge and agreement. AI output is draft material until a human reviews it; do not invent agreement, owners, or deadlines. |
| Release | The first release decision follows a playable, tested game. Steam is only a possible stretch goal. |
| Initial setup | Documentation and planning only; no engine selection, game implementation, CI, bots, automatic Discord integration, or build automation. |

## Still open

The leading concept is a Stardew Valley-inspired fantasy college-town game, with classes and conversations supplying knowledge that could help the player defeat dragons and graduate. This direction and its broader mechanics remain proposals; see the [November 2 summary](meetings/2026-11-02.md). Engine, controls, visual/audio direction, initial platform, full-game scope, and run instructions remain undecided. Godot is a candidate. A Minecraft-style game with magic was only a hypothetical example, not an approved game idea.

Discord use needs member confirmation; invitation and email/contact details are TBD. Additional volunteers, task owners, and target dates are unassigned unless someone explicitly agrees. Repository licensing, contributor ownership, and any revenue terms remain unresolved.

## D001 First prototype scope

- **Status:** Agreed.
- **Decision:** One room with boundaries; player movement; one NPC; an interaction button that opens a short conversation; and a way to close it and resume moving. Placeholder art is sufficient.
- **Completion:** Another person can launch the prototype, walk around, talk to the NPC, close the dialogue, and continue moving without getting stuck.
- **Reason:** Establish movement and conversation before attempting class systems, semesters, dragons, quests, or progression.
- **Confirmed by:** Micah Kelley, explicitly confirming inclusion of NPC interaction after proposing the room prototype.
- **Date confirmed:** November 2, 2026.
- **Source:** [Meeting summary](meetings/2026-11-02.md) and Micah's authorization to publish these notes. No separate vote or review by other members is claimed.
- **Supersedes:** None. This adds prototype scope; it does not choose an engine or approve the full game concept.

See [PROTOTYPE.md](PROTOTYPE.md) for scope and unassigned task drafts.

## D002 Repository tests on pull requests

- **Status:** Agreed by Micah Kelley on November 2, 2026 through his request for a repository test suite that passes for PRs.
- **Decision:** Add a small Python standard-library suite for current documentation links and issue-template metadata, and a GitHub Actions check on PRs and pushes. Retain the existing PR/task/bug/idea templates. Engine-specific game tests follow engine selection and implementation.
- **Reason:** Give contributors repeatable checks and make failures visible before merging.
- **Supersedes:** The initial setup's exclusion of CI and a documentation test suite, for these repository checks only. Engine choice, game implementation, bots, and build automation remain outside this change.
- **Enforcement:** A maintainer must require the **Repository checks** status in `main` protection; adding the workflow does not configure that setting. See [TESTING.md](TESTING.md).

## Recording future decisions

Add a short entry only after agreement. Keep proposals and unresolved questions in the relevant issue or meeting note until then.

```text
Decision ID and title:
Status: Agreed / Superseded
Decision:
Reason and relevant alternatives:
Agreed by:
Date agreed: YYYY-MM-DD (actual agreement date)
Source: link to reviewed meeting note or issue/PR
Supersedes: prior decision ID, or none
```

When a decision changes, retain the earlier entry, mark it superseded, and link both entries. Do not backdate agreement or silently replace the record.
