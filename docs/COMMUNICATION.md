# Communication and shared records

| Place | Purpose |
| --- | --- |
| Discord — proposed, awaiting member confirmation | Day-to-day discussion, questions, sharing work, and feedback. Suggested channels: `announcements`, `game-planning`, `development`, and `playtesting`. Invitation: TBD. |
| Email | Announcements and reaching people who are not following chat. Contact/list details: TBD. |
| GitHub | Official reviewed plans, decisions, tasks, and changes: [Meeka89/HUAIC-Game-Project](https://github.com/Meeka89/HUAIC-Game-Project). |

Discord messages and email suggestions do not automatically change requirements. Agents should read shared repository documents, not rely on access to private chats.

## From discussion to an agreed change

1. A volunteer or maintainer captures the relevant context and labels it as a proposal, open question, or possible task. Check for an existing issue first.
2. Participants review scope and dependencies. Obtain agreement from the people responsible for the decision; do not treat silence as approval.
3. A maintainer or contributor proposes a focused documentation PR or issue. Record actual agreement and its source in [DECISIONS.md](DECISIONS.md), and update [GAME_DESIGN.md](GAME_DESIGN.md) when appropriate.
4. After review, merge the documentation. Give agreed tasks completion criteria; record owners and target dates only when explicitly accepted. Maintainers can submit contributions received through Discord and confirm the edit with the contributor.

Local documents can hold planning drafts. Publish reviewed records through the repository workflow so everyone can use the same context.

## Manual meeting and AI summary workflow

1. Explain any intended recording and obtain participants' knowledge and agreement before recording. Use manual notes when recording is not agreed. Keep raw recordings and transcripts outside the repository; do not commit them.
2. If using AI, use only material participants have agreed may be shared with that tool. Remove unnecessary personal information. Ask for four separate categories: **agreed decisions**, **proposed ideas**, **open questions**, and **action items with owners and target dates**. Missing owners/dates stay unassigned/TBD.
3. A human checks the draft against the discussion, corrects mistakes, and asks participants to clarify ambiguous agreement. Never upgrade suggestions into decisions. Use the [meeting template](meetings/TEMPLATE.md); mark the note draft until reviewed and record who reviewed it once known.
4. Submit the reviewed summary and proposed design updates through a PR. Keep unapproved material clearly labeled, move agreed decisions into the decision record, and create or update tasks only after checking for duplicates.
5. Share a link to the reviewed record through the chosen channels. Raw files remain outside Git; check the staged diff for accidental private content.

No automated Discord integration is needed. Volunteer note-taking, summary review, or task entry can rotate between meetings; it does not have to fall to Micah every time.
