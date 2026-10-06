# Critique Checklist

Run it on every size before delivery, and when reviewing someone else's work.
State findings as "what, where, why, fix", for example: "Price at the bottom
right competes with the headline because both use the accent. Fix: set the
price in ink and keep the accent on the headline word."

## A. Automatic (the engine already checks; read the result, don't redo it)

| Check | Where | Gate |
|---|---|---|
| Text fits its box, no clipping | compose/make rejects | hard |
| No text overlapping text | `text_overlaps_text` | hard |
| Nothing opaque covers text | `covered_text` | hard |
| Text inside the canvas | `text_outside_canvas` | hard |
| Contrast AA on the real backdrop | `low_contrast`, `trace.json` contrast | hard |
| Not a near-copy of recent work | layout memory, similarity ≥ 0.8 | hard |
| Design score 0–100 (hierarchy, whitespace, balance, alignment, margins, rhythm, density, color, focus) | `compose` summary, eval reports | ranks options |

A layout can pass every gate and still be wrong. Do not stop at section A.

## B. Human eye (the engine cannot judge these)

1. **Three-second test.** Look away, glance for three seconds. Can you say the
   message and the action? If not, the hierarchy is wrong.
2. **First, second, third.** Where does the eye land first, second, and third?
   Does that match the intended read order?
3. **Squint test.** Blur your eyes: one clear dark/light mass should remain.
   Many equal blobs mean no focus.
4. **Every word correct.** Spelling, prices, dates, phone numbers, Thai
   vowels and tone marks, no broken word at a line end.
5. **Photo quality.** Subject sharp and whole (no cut-off heads or hands),
   cut-out edges clean, no stretched or pixelated image.
6. **Feeling.** Does it feel like the concept and the brand (calm, loud,
   premium, cute)? Does the look fit the audience?
7. **In context.** View it at phone size inside a feed or story mock. Story
   text stays clear of the app UI zones.
8. **Series.** Placed next to the client's previous posts, does it look like
   the same brand but not the same post?
9. **Rights.** Photos, fonts, and textures are licensed for commercial use; no
   protected emblems or another brand's identity.

## C. Common problems and fixes

| Problem | Fix |
|---|---|
| Everything is the same size | Make the headline 2–3× bigger, demote the rest |
| Feels crowded | Cut copy, widen margins, drop a decoration, not the size floor |
| Feels empty or unfinished | Make the hero bigger, add a panel or texture behind text, tighten the group |
| Accent everywhere | Accent on one word or the CTA only |
| Text fights the photo | Fade the photo, add a panel, or move text to the calm side |
| Looks templated | Change the composition idea or the crop, not just the colors |
| Cheap "wow" effects | Keep one effect on one element; remove the rest |
| Thai looks cramped | Increase line height; shorten lines; use a Thai display face |
| Brand color unreadable as text | Use it as a shape or button, set text in ink or white |

## D. Feed the system

When a person overrides the design score (a high score that looks wrong, or a
low score that is right), write down the case in the job notes. Recurring cases
become new checks or new score criteria in `aesthetics.py`, with a test.
