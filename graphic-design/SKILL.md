---
name: graphic-design
description: Design principles and a working method for Solo Empire graphics (social posts, posters, campaigns, cover-style art) - message, hierarchy, typography (Thai and Latin), color, composition, photos, art styles, variety across a series, and critique. Use when briefing, designing, composing, reviewing, or explaining a graphic or an art style; when an AI or human needs to judge whether a layout is good and why; or when changing the graphics engine's composer, art styles, prompts, or design score.
---

# Graphic Design

A graphic is good when the right person gets the message in about three seconds,
wants to act, and remembers the brand. Taste follows from that job; it is not
decoration. This skill holds the principles; the graphics engine
(`book-production graphics ...` in book-production-platform, guide
`docs/GRAPHICS-THEMES-GUIDE.md`) carries them out.

## Workflow

1. **Brief before pixels.** Pin down: who sees it, where (feed, story, print),
   the one message, the one action, the proof (price, date, offer), the brand
   colors and the look wanted. Missing message or action → ask; do not design
   around a gap. Use `templates/roles/content-distribution/graphic-brief.md`.
2. **Concept.** One sentence: what the viewer feels and sees first. Choose the
   hero: a photo, a word, a number, or a shape. Exactly one hero.
3. **Look.** Pick or create an art style (palette, type, texture, motifs) that
   fits the audience and concept — see `references/art-styles.md`. A look may
   repeat across a client's posts; a composition should not.
4. **Compose.** Lay out hierarchy, grid, space, and depth per size — see
   `references/principles.md`. Prefer `graphics compose` (new layout per job,
   memory against repeats) or `compose-campaign` for a series; use `make` with a
   theme when the client chose a fixed template.
5. **Critique.** Run the checklist in `references/critique.md`: the engine's
   automatic checks first (fit, overlap, contrast, design score), then the
   human-eye questions the engine cannot answer. Fix, re-render, look again.
6. **Deliver.** Every size, editable SVG, font list, and the request JSON for
   later edits. Record time spent and what the client changed.

## Decision rules

- Two things fighting to be first → shrink or remove one; never make both big.
- Text unreadable on a photo → move the text, add a solid panel or fade, or
  pick another crop; never lower the contrast bar.
- Too much copy for the format → cut copy with the client or split into a
  carousel/series; never shrink body text below the size floor.
- Brand colors that fail contrast → keep them for shapes and accents, set text
  in ink/white.
- Thai text → no uppercase or wide tracking tricks; allow taller line height;
  never break inside a word; use a Thai-capable font for every Thai glyph.
- "Make it pop / more wow" → raise scale contrast, depth, or one bold color
  move; do not add more elements.
- A series → hold palette, type, and logo position constant; vary the
  composition idea, crop, and hero element per post.
- Stock or client photos → only with commercial rights; no protected marks
  (Red Cross emblem, government seals), no imitation of another brand.
- Design score high but it looks wrong to a person → the person wins; note why
  so the score can learn the case.

## Resources

- `references/principles.md` — read when composing or explaining why a layout
  works: message, hierarchy, typography, color, composition, photos, depth,
  formats, series variety.
- `references/art-styles.md` — read when choosing, describing, or creating a
  look (what makes retro, minimal, jazz, dystopia, swiss … recognisable).
- `references/critique.md` — read before delivering or when reviewing someone
  else's graphic: automatic checks vs. human checks, and common fixes.
