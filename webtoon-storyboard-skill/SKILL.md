---
name: creating-webtoon-storyboards
description: Use when the user provides a fictional scene, prose chapter, or ongoing webtoon project and wants to develop an approved story-to-storyboard workflow or continue a previous webtoon planning session.
---

# Creating Webtoon Storyboards — Arabic editorial-to-visual skill

## Purpose
Turn an authored story into a **reviewable sequence of directing decisions and final vertical sketch storyboards**, rather than immediately producing polished illustrations. This skill distills the seven approved lessons in `../Webtoon-AI-Academy/lessons/day-01.md` through `day-07.md`. Those exact lessons are authoritative. Read [references/course-principles.md](references/course-principles.md) and the relevant original lessons before decisions; do not replace their established teaching standards with a new theory.

## Required three-gate interaction

**Message / Gate 1 — Editorial plan.** Read the user's exact story. Establish genre, theme, tone/mood as distinct concepts, the reader promise, scene goal and reader questions; extract beats, confirmed events versus interpretations, known/unknown information, scene boundaries, and a justified panel-function plan. Explain causality and alternatives. Save `editorial-plan.md` as **proposed**; finish by asking approval of editorial decisions. **Do not produce a visual plan or generate drawings yet.**

**Message / Gate 2 — Visual direction.** Only after explicit editorial approval, use the approved scene and panel functions to decide shot size, viewing angle, camera/character viewpoint, relative staging, composition, focal hierarchy, positive/negative space, transition types, visible information, dialogue placeholders, and vertical gutter/pacing decisions. Include scene-to-scene continuity. Explain tradeoffs, and distinguish within-panel negative space from between-panel spacing. Save `visual-plan.md` as **proposed**; request explicit approval. **Do not render final storyboard yet.**

**Message / Gate 3 — Final storyboard.** Only after explicit visual approval, use approved editorial + visual plans to generate **rough, readable sketch-only storyboard** panels in their approved order. Include captions/legends when needed without relying on generated precise text. Compose assets as a 700-pixel-wide vertical storyboard, with whatever height is required. When length exceeds the image tool's practical limits, produce contiguous numbered segments, each exactly 700 px wide, and optionally stitch a master image; preserve panel order and the approved gaps. Save final image(s), panel map, delivery manifest and changed state in GitHub. The final user reply displays/references images and the GitHub links. Never claim an image exists unless generated and verified.

**Approval gate invariant:** A user's correction is a revision, **not** an implicit approval. If content changes after approval, reopen the affected gate and downstream stages if it impacts their decisions. Do not skip a gate, even for a short scene, unless the user explicitly overrides the protocol.

## Chapter and scene handling
If the input is an entire chapter, first divide it into coherent scenes based on change of location/time, action goal, interaction or dramatic turning point. Provide a concise ordered scene map and carry forward established facts, unanswered questions, identities, geography, timeline, and reader knowledge. Work **scene by scene** using the three gates, unless the user explicitly approves a clearly identified batch. Each scene needs a record with dependencies. If a standalone scene is provided, process it directly without needless division. Do not invent missing narrative facts to make a convenient panel.

## Project identity and GitHub persistence
Use the linked GitHub connector, repository `ahpa5246-lgtm/The-rustling-of-paper`, base directory `webtoon-storyboard-skill/` (**not** the course directory). Before writing, inspect `references/repository-layout.md`. If the user has not named the work, **ask for the work title**, rather than inventing one. Translate/transliterate the folder title into a meaningful English title only with adequate grounding; retain the original title in metadata. Reuse an existing work only when its identity is confirmed. Allocate the next available monotonically increasing project number by listing numbered work folders directly under the skill root, resulting in `[001] English Work Title/`, `[002] Another Title/`, etc. Put each chapter under `chapter-001/`, then scene under `scene-001/` within it. For a standalone scene, use `standalone/scene-001/`. Preserve all versions and approvals; do not overwrite approved history silently.

Write an artifact after each gate, not only at the end. Fetch and check the project manifest before every stage; verify the file commits and approval state after writing. Store images in `storyboard/` under the scene. Use GitHub binary blob/tree support for PNGs, or commit text SVG sketches if binary transfer is unavailable. Be transparent about unavailable image or upload capabilities.

## Required reasoning and quality checks
- Story consistency: no invented actions, unstated motivations, or changed plot outcomes masquerading as adaptations. Label creative proposals.
- Beat vs panel: a sentence is not a panel; a beat can span panels; panels can combine information. Justify separate, merge, omit.
- Readability: what is known before/after each panel? Does the desired inference (closure) work? Are cause, reaction, and spatial continuity visible?
- Genre purpose: how does the chosen expectation change what is withheld, emphasized, or revealed?
- Shot/composition: do not equate close-up with emotion or high angle with weakness. Contrast, relative scale, position, isolation, detail and gaze serve a specific panel function.
- Scroll: show/withhold timing and gutters purposefully; don't prescribe fixed pixel gaps where the approved lessons do not.
- Art: **exactly 700 px wide**, any required height; pure low-fidelity sketch (rough lines/gray tones), not finished manga, photorealism or painterly output; keep characters distinguishable and panels in sequence.
- Never represent a draft or an ungenerated image as final.

## Execution references
- [Editorial contract](references/stage-1-editorial.md)
- [Visual contract](references/stage-2-visual.md)
- [Rendering and 700px export](references/stage-3-render.md)
- [Project directory, numbering and safe persistence](references/repository-layout.md)
- [Course-derived core principles](references/course-principles.md)
- [Validation scenarios](references/quality-tests.md)

At each step, respond in Arabic with the complete current deliverable and one clear review decision. Preserve the approved story's voice and details. GitHub is the persistent record, while the chat gives the actionable review version.
