# Game design

The leading direction from the [November 2 discussion](meetings/2026-11-02.md) is a Stardew Valley-inspired fantasy college-town game. The full concept remains a **proposal**. Only the first room-and-NPC prototype is confirmed; see [D001](DECISIONS.md#d001-first-prototype-scope).

| Question | Current direction and status |
| --- | --- |
| Concept: what is the game in one sentence? | Proposed: a fantasy college-town game inspired by Stardew Valley, combining school and adventure. |
| Player goal: what is the player trying to achieve? | Proposed: progress through semesters, graduate, and help save the world while facing dragons. |
| Core loop: what does the player repeatedly do? | Proposed: attend classes, talk with teachers and students, learn useful information, and apply it to adventures. Exact daily activities remain undecided. |
| Main mechanic: what single interaction carries the game? | Proposed: different classes and conversations supply knowledge that helps defeat dragons and progress the game, while building lore. |
| Smallest playable version: what complete, tiny experience can we test? | Confirmed: one room with boundaries, player movement, and one NPC with a short conversation that can be opened and closed; movement resumes afterward. Placeholder art is sufficient. See [prototype scope](PROTOTYPE.md). |
| Controls and input devices | Undecided |
| Visual direction | Proposed: a mix of 2D and 3D, possibly retro pixel art / an 8-bit look. Camera and asset style are undecided. |
| Audio direction | Undecided |
| Engine and initial target platform | Undecided. Godot is a candidate, not selected. |
| Additional exclusions: what will we deliberately leave out? | Classes, semesters, dragon encounters, quests, and progression are outside the first prototype. Later scope remains open. |

Confirmed boundary: a small single-player game; multiplayer is excluded from the initial scope. Any Minecraft-style game with magic mentioned previously was a hypothetical task-breakdown example, not a selected concept.

## Other proposed elements

Dragons, bisons, Harding-inspired Easter eggs, a storyline, and a possibly medieval world were discussed. Exploring Harding University was raised; how closely the college town resembles Harding remains undecided. Animations were mentioned without a defined scope.

Roguelike and incremental games were also raised as alternatives; they are not confirmed systems to add to the leading concept. The library example was explanatory, not selected. Specific class names, farming, relationship systems, and a calendar have not been agreed; do not infer them from the Stardew Valley reference.

## Open design questions

- What does the player do during an ordinary day, and why is it enjoyable?
- Do different classes create alternative solutions, or must everyone learn the same information?
- How is knowledge applied during dragon encounters? Combat, conversation, puzzles, and other approaches are undecided.
- What roles do dragons and bisons play, and how much of the town is needed?
- Which engine, platform, controls, camera, and visual approach should the first prototype use?
