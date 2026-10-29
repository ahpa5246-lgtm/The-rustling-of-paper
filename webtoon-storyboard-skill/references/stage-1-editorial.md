# Stage 1 contract — editorial decisions (Arabic response)

## Entry and scope
Accept either a complete chapter or a single scene. If the work title is missing, ask for it and do not invent one; a source chapter title is not automatically a work title. Resolve whether this is the same previously confirmed work before creating a new numbered folder. Read the supplied text fully before splitting or planning.

For a chapter, make a **scene map first**:
- scene ID, source span (first/last sentence cue or paragraph identifiers), place/time, active participants, immediate goal, event/turning point, next scene dependency;
- global chapter continuity: timeline, revealed secrets, pending reader questions, prop/character continuity, who knows what;
- work scenes sequentially and identify the current scene. A global scene map is not permission to bypass scene-level approval.
For a single scene, begin the current scene directly, no artificial subdivision.

## Required plan content
1. **Provenance:** source title/chapter if supplied, exact scope, narrative facts, unclear source details, what was intentionally left unknown.
2. **Genre vs theme vs tone vs mood:** meaningful, *defensible* interpretations from supplied text. State alternatives where tone/genre truly ambiguous. Confirm user preference rather than treating inference as authorial fact.
3. **Reader promise and dramatic question:** what the reader expects to experience, which question this scene poses, what is answered and what must remain pending.
4. **Initial state → disruption → beat sequence → final state:** each beat ID and corresponding source evidence, change in action/knowledge/decision/emotion/relationship, character and reader knowledge before/after; flag assumptions.
5. **Visual units / draft panel functions:** ordered IDs (P01...), narrative function from the day-03 set, information to show vs imply vs withhold, action/reaction and reason for separation/merge/omission. These are *written decisions only*: no concrete shot sizes/angles/precise composition yet.
6. **Scene continuity:** characters, props, setting geography, unresolved reader questions; do not reveal future spoilers ahead of intended beat.
7. **Alternatives:** at least one meaningful tradeoff (e.g., earlier/later reveal), with recommendation grounded in genre and source.
8. **Editorial approval question:** ask the user to approve or correct classification, reader promise, beat order, and panel-function allocation. Mark `stage1.status=proposed`.

## Constraints
- No unrequested rewriting or truncation of source text. Cite/quote small source cues so the user sees grounding.
- Classify *confirmed fact*, *character belief*, *reader inference*, and *creative proposal* separately.
- Never force one sentence = one panel or beat = one panel.
- If a chapter is long, use sequential scene IDs and keep a persistent context ledger. Avoid doing all scenes at shallow level to fit a token limit.
- Do not proceed to Stage 2 without explicit approval. A request to "change scene 2" reopens the affected editorial decisions.

## Suggested response shape
A brief paragraph establishing scope, then sections: Narrative identity; Scene map (chapter only); Beat analysis; Written panel functions; Alternatives and unresolved issues; Approval decision. Explain reasons in prose adjacent to tables. Don't present vague conceptual questions with no example of the answer's consequences.

## Files written at this gate
`chapter-XXX/source.md` (user-provided material with provenance, if storing is authorized), `chapter-XXX/scene-map.md` for chapters, `scene-XXX/editorial-plan.md`, `scene-XXX/continuity.json` and the project/chapter state manifest. Record the source hash when accessible and revision number. Approval must be a separate state transition, not inferred from upload success.
