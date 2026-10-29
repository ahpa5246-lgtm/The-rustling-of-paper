# Acceptance tests for the reusable storyboard skill

This is a skill-spec regression suite. A future agent must demonstrate the specified behavior on these test prompts. Don't claim live image-generation/provider tests unless actually run. Store evidence or a dated validation log before describing them as passed.

## Baseline failures the protocol prevents
- A user gives a scene and agent generates attractive panels immediately: violates both approval gates.
- A user gives a chapter and agent treats whole chapter as one scene: loses transitions and reader-knowledge continuity.
- A genre is chosen from one phrase and silently asserted as authorial intent: editorial fact confusion.
- Every sentence becomes a panel: ignores beat and closure.
- Visual plan overemphasizes a background sign while vital message is unreadable: shot size without composition.
- "7 panels at 700px" turns into a 1024px-wide polished painting: image specification failure.
- An existing work gets a fresh project folder for each chapter: persistence failure.
- User revises the beat order but renderer continues from previously approved visual frames: stale approval breach.

## Scenario matrix and expected checks

| ID | Scenario | Required outcome |
|---|---|---|
| S01 | User submits one scene but no work title | Ask for title, no invented project name; preserve scene analysis scope |
| S02 | User submits full chapter with 6 locations | Scene map ordered by causality and location/time; start scene 1 and carry scene context |
| S03 | User says "genre is drama, I approve stage 1" | Record explicit editorial approval before proposing Stage 2 |
| S04 | User says "interesting" about draft | No approval; stay in current stage |
| S05 | User changes a beat after Stage 2 approval | Reopen affected editorial approval and visual gate; no render |
| S06 | User returns with chapter 3 of known work | Reuse numbered work folder, new `chapter-003`, preserve previous continuity |
| S07 | A 30-panel storyboard is too tall for one image generation | Segment at panel boundaries, all pieces exactly 700px wide, ordered roster without duplication |
| S08 | Image source supports only 1024px wide | Export final to exact 700px after resizing/composition, verify actual file metadata |
| S09 | Exact Arabic dialogue in a generated phone screen is unreadable | Use deterministic overlay, not fabricated readable text |
| S10 | GitHub connector can't commit binary | Store valid image SVG if feasible and label; otherwise report failure, no false success |
| S11 | User gives "scene 2 is same characters as scene 1" | Use prior chapter state: props, locations, character and reader knowledge |
| S12 | Source implies grief but not specific crying action | Label crying as a proposed visual choice, not confirmed event |

## Mandatory static checks on deliverables
- Root SKILL frontmatter includes `name` and `description` (trigger only).
- All required `references/*.md` exist and all links resolve.
- Scene state requires stage1 approved for stage2, stages 1+2 approved for stage3.
- Project naming is `[NNN] English Work Title` and chapter isolation is enforced.
- For final image, PNG signature valid, every part width exactly 700; scene/panel IDs and order match approved visual plan.
- Report failures by test ID, not a blanket "all tests passed" without evidence.

## Manual dry run
Give a one-scene fake text about a student hiding a letter, confirm stage1 contains genre/theme/promise/beat/panel functions only and ends at first gate. Then simulate explicit approval, verify stage2 includes shot composition/gutters with no image. After second simulated approval, validate a placeholder (not user-facing final art) at 700px and ensure generated file is not misrepresented as an illustration from an image model. This tests the protocol, not actual generation quality.
