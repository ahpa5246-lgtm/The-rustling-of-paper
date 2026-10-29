# GitHub workspace, numbering and persistence

**Repository:** `ahpa5246-lgtm/The-rustling-of-paper`  
**Independent root:** `webtoon-storyboard-skill/` (sibling of `Webtoon-AI-Academy/`). `SKILL.md`, `references/`, `scripts/` and `README.md` are skill machinery; projects are under `projects/` to avoid mixing user output with skill definitions.

## Project path contract

```text
webtoon-storyboard-skill/
  SKILL.md
  README.md
  references/...
  scripts/validate_storyboard.py
  projects/
    [001] English Work Title/
      work.json
      continuity.md
      chapter-001/
        source.md
        scene-map.md
        chapter-state.json
        scene-001/
          scene-state.json
          editorial-plan.md
          visual-plan.md
          continuity.json
          storyboard/
            storyboard-part-01.png
            storyboard-part-02.png
            storyboard-full.png          # optional
            panels.json
            render-checks.json
          delivery.md
      chapter-002/...
      standalone/
        scene-001/...
    [002] Another English Work Title/...
```

Git does not store empty directories; create files only when there is real content. The bracketed three-digit project prefix is literal: `[001] English Work Title`. Always assign the first available number greater than the **maximum existing number**; do not reuse deleted numbers. Scan all entries under `projects/` via the connected GitHub API, handle pagination, and recheck immediately before creation to avoid collisions. Do not rename old projects when adding new ones. Project title must be English while the source title may remain Arabic in `work.json`.

If a work title is not supplied, **ask the user**; do not use a chapter title as a surrogate work title. If a work with the same title already exists, inspect metadata and ask which existing work is intended when ambiguous. Chapters from the same confirmed work always go in the same numbered project. Determine chapter ID from provided chapter number if unambiguous, otherwise allocate next `chapter-NNN`; for standalone scenes use `standalone/scene-NNN`. No separate numbered work folder per chapter.

## Manifests and states
`work.json`:
```json
{
  "schema": "webtoon-storyboard-skill/work-v1",
  "work_id": "001",
  "english_title": "English Work Title",
  "source_title": "عنوان العمل الأصلي",
  "repository": "ahpa5246-lgtm/The-rustling-of-paper",
  "chapters": [],
  "standalone_scenes": [],
  "next_scene_number_policy": "monotonic-within-container"
}
```
`scene-state.json`:
```json
{
  "schema": "webtoon-storyboard-skill/scene-v1",
  "scene_id": "scene-001",
  "source_revision": 1,
  "editorial": {"status": "proposed", "revision": 1, "approved_revision": null},
  "visual": {"status": "blocked", "revision": 0, "approved_revision": null},
  "storyboard": {"status": "blocked", "revision": 0, "approved_visual_revision": null},
  "panel_ids": [],
  "updated_at": null
}
```
Valid statuses: `blocked`, `proposed`, `approved`, `needs-revision`, `complete` (complete only for storyboard once verified and uploaded). After approval set `approved_revision` to current revision and record date/source of explicit approval. Editorial revision invalidates visual and storyboard approvals. Visual revision invalidates storyboard state. Do not overwrite prior approved assets silently; use revision files or Git history with an index identifying the current revision.

## Scene continuity record
Record location/time and transitions, character IDs/appearance constraints, props and ownership, relationships, confirmed knowledge per character, knowledge already revealed to reader, withheld information, active dramatic question, unresolved clues, and established directions in physical space. Re-read previous scene and chapter manifests when starting the next scene; do not assume conversational context survives.

## Persistence gates
- Initial input → create work/chapter metadata, scene map (when chapter) and editorial `proposed`.
- Explicit approval #1 → `editorial.approved`, then create visual `proposed`.
- Explicit approval #2 → `visual.approved`, then render storyboard.
- Verified generation AND GitHub upload → storyboard `complete`.

Use GitHub connector for every write. For text files use contents API. For binary assets use Git Data blob/tree/commit/ref workflow described in stage-3. Read back the file or blob SHA and use optimistic expected branch SHA; reconcile on concurrency error rather than force-pushing. Never put image data into an ordinary Markdown code fence and call that a saved image. Report partially saved outputs accurately.
