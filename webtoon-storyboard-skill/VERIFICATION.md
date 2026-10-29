# Skill verification — 2026-10-29

## Confirmed GitHub state
- Day 6 and Day 7 complete lessons have `Approved` headers; `Webtoon-AI-Academy/COURSE_STATE.md` records 7/30 approved.
- The skill root contains `SKILL.md`, `README.md`, all six required references, a 700px validation script, JSON state/roster templates, and optional agent metadata.
- GitHub reads of the required files succeeded after commits; no example project/work was created without a user-supplied title and story.
- Numbered work folders are direct children of `webtoon-storyboard-skill/` with literal `[NNN] English Work Title` naming.

## Static contract review
- Stage 1: prose classification/theme/reader promise, beats, panel functions, scene map when needed, and approval gate.
- Stage 2: shot size, angle, blocking, composition/hierarchy, gutter decisions, and second approval gate.
- Stage 3: 700px-width low-fidelity storyboard, unlimited conceptual height, safe segmentation at panel boundaries, sequential panel manifest, GitHub binary/SVG storage and post-write verification.
- Script reads PNG/SVG dimensions and checks state approval, ordered panel roster, and image width; Pillow decoding is used if installed.

## Not claimed as tested
- No user story, project title, or approved editorial/visual plan has yet been provided for the new skill; therefore **no storyboard image has been generated**.
- Live image generation, binary GitHub upload and full chapter continuity across multiple sessions require a real story and tool access at execution time. The scenario tests in `references/quality-tests.md` are acceptance cases, not recorded end-to-end executions.
- Existence of a `SKILL.md` file in GitHub does not automatically register it as an installed ChatGPT plugin. Use it from this conversation via GitHub retrieval or install it in a skill-capable agent environment.
