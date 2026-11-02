# First prototype

Scope confirmed by Micah Kelley on November 2, 2026; see [D001](DECISIONS.md#d001-first-prototype-scope) and the [meeting summary](meetings/2026-11-02.md). This describes work to plan and implement, not an existing playable build.

## Included

- One room with boundaries.
- A player who can move around the room.
- One NPC.
- An interaction button that opens a short conversation.
- A way to close the conversation and resume moving.
- Placeholder art is sufficient.

## Completion checks

Another person can launch the prototype using documented setup or build instructions, walk around without passing through boundaries, approach and talk to the NPC, close the dialogue, and continue moving without getting stuck. Verify the interaction can be repeated.

These are checks to perform when implementation exists. They have not run; there is no build yet.

## Outside this prototype

Classes, semesters, dragon encounters, quests, and progression. The broader fantasy college-town proposal is in [GAME_DESIGN.md](GAME_DESIGN.md). Multiplayer remains outside initial project scope. No full campus, world-saving storyline, or full-game content is required to finish this prototype.

## Dependencies and integration choices

Engine, initial platform, camera, 2D/3D approach, and exact controls remain undecided. Godot is only a candidate. Use [initial planning task 2](INITIAL_TASKS.md#2-evaluate-suitable-engines-after-narrowing-the-concept) to evaluate and agree on an engine before implementation.

Agree on how NPC interaction is triggered, what happens to movement during dialogue, and how closing dialogue restores normal play. Inspect existing work first and avoid separate incompatible movement or interaction systems. Write actual setup/run instructions once the engine is selected.

## Proposed task breakdown

These are unassigned drafts, not live issues. Review against existing tasks before claiming work. All owners are unassigned and target dates TBD.

| Draft task | Depends on | Observable completion |
| --- | --- | --- |
| Establish project and placeholder room | Agreed engine, platform, and visual approach | Documented setup opens one room with placeholder assets and boundaries. |
| Add player movement | Project and room; agreed controls | Player moves around and stays within the room. |
| Add one NPC and conversation | Room and player; agreed interaction integration | Player opens and closes a short conversation and resumes moving. |
| Verify the complete prototype | Movement and conversation integrated | Another person follows setup/build instructions and checks the interaction; results and bugs are recorded. |

This documentation update does not implement or assign these tasks or add engine-specific commands.
