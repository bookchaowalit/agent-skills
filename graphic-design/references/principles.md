# Graphic Design Principles

Each principle states the rule, why it works, how to apply it, and how the
graphics engine enforces or measures it (`check` = hard gate that rejects a
layout, `score` = part of the 0-100 design score in `aesthetics.py`,
`human` = only a person can judge it).

## 1. Message first

- **One message, one action per graphic.** A viewer gives a feed post about
  three seconds. Everything that does not serve the message or the action is a
  cost. Several messages → a carousel or a series. *(human)*
- **Read order is designed.** Decide the order: hero → headline → proof
  (price, date, offer) → action → small print. Size, weight, color, and
  position must produce that order without effort. *(score: hierarchy)*
- **Proof beats adjectives.** "-30% ทุกวันธรรมดา" says more than "สุดคุ้ม".
  Give the number, date, or place its own visual weight. *(human)*
- **The action looks pressable.** CTA as a button shape or a clearly separated
  line, near the end of the read order, never competing with the headline.
- **Labels sit in the optical middle of their button or tag.** Center by the
  visible glyphs, not the line box: digits start far below the ascender, Thai
  tone marks rise above it. *(automatic: `box_text.py` re-centers every label
  on a button, tag, or chip after compile; panels holding a stack are left alone)*

## 2. Hierarchy and scale

- **One dominant element.** The largest element should be clearly larger than
  the next: aim for 1.5–4× between headline and the next text, 2–6× between
  headline and the median text. Two equals read as noise. *(score: hierarchy)*
- **Three levels are enough.** Display, supporting, small. More levels blur.
- **Scale contrast creates energy.** A huge word next to a tiny label is more
  striking than everything medium. "Make it pop" usually means more scale
  contrast, not more elements.
- **Weight and color are hierarchy tools too.** An accent color on the one word
  that matters (`*word*` markup) beats making the whole line bigger.

## 3. Typography

- **Size floor.** Body copy is never smaller than about 1.6% of the short side
  at the delivery size (≈17 px on 1080 px); labels have the same floor.
  *(check: composer scaling floor)*
- **Line length.** About 20–40 characters per line on a post; long lines need
  a narrower box, not a smaller size.
- **Pair, don't collect.** One display face + one text face (+ optional mono or
  label face). Contrast them by structure (serif/sans, condensed/round), not by
  near-duplicates.
- **Text fits its box and never collides.** *(check: text fit, text-on-text
  overlap, outside canvas)*
- **Thai typography.**
  - Thai has stacked vowels and tone marks above and below: give display Thai
    a line height of at least ~1.15 and keep generous space between lines.
  - No uppercase, and no wide letter spacing on Thai, because Thai script has
    no case and tracking breaks word shapes. Latin may use caps and tracking.
  - Line breaks fall between words (PyThaiNLP segmentation), never mid-word,
    and never leave a lone fragment. Loanwords such as "ดริป" stay whole. When a
    word is wider than its box, the text shrinks until the word fits; a word is
    cut only when even the minimum size cannot hold it. *(automatic: `fit_text`)*
  - Every Thai glyph needs a Thai-capable font (Kanit, Mitr, Prompt, Sarabun,
    Trirong, Anuphan …); Latin display faces fall back per glyph.
  - Cropped or bleeding giant Thai words lose their shape. Use bleed only for
    short Latin words or numbers.
- **Display tricks with purpose.** Outline, motion blur, rotation, and echo
  are spice for one element, never the body copy.

## 4. Color

- **Contrast is non-negotiable.** Text 4.5:1 against its actual backdrop,
  large text (≥24 px) 3:1, button text on button 3:1 (WCAG AA). *(check:
  low_contrast, text_on_shape_low_contrast)*
- **60-30-10.** About 60% dominant (background), 30% secondary (panels,
  photo), 10% accent (CTA, the key word, the price). The accent is
  for attention; overusing it removes the attention.
- **Few colors.** 2–5 solid colors per graphic. *(score: color)*
- **Brand colors are not always text colors.** A brand orange that fails
  contrast on cream goes on shapes and buttons; text stays in ink.
- **Color carries mood.** Warm/saturated = energy, sale, food; cool/desaturated
  = calm, trust, premium; black + one accent = drama; pastel = soft, kawaii.
  Choose by the concept, then check contrast.

## 5. Composition and space

- **Grid and alignment.** Elements snap to shared edges or axes. Every extra
  text axis costs clarity: one or two alignment axes per graphic.
  *(score: alignment)*
- **Margins.** Keep text at least ~3.5% of the short side from the edge, and
  further on story formats (see 8). *(score: margins)*
- **Whitespace is an element.** Roughly 30–70% of the canvas covered by
  content. Empty space around the hero makes it the hero. Crammed = cheap;
  empty slab with nothing to do = unfinished. *(score: whitespace, density)*
- **Balance.** Either symmetric and calm, or deliberately asymmetric with a
  counterweight (big photo left, compact text right). The visual center of
  mass should not drift to an edge by accident. *(score: balance)*
- **Proximity groups meaning.** Things that belong together sit together
  (price next to product, date next to place); unrelated things get space.
- **No dead bands.** A tall story with all content in its top half reads as
  unfinished; spread the stack or enlarge the hero. *(score: spread)*
- **Rhythm.** Repeated gaps between stacked texts share a unit; random gaps
  look accidental. *(score: rhythm)*
- **Reading paths.** Z pattern for sparse posters (top-left → top-right →
  bottom-left → bottom-right CTA); F pattern for text-heavy cards; centered
  stack for single-message announcements.
- **Composition ideas, not templates.** Split, full-bleed photo, type poster,
  frame/card, diagonal, circle focus, editorial column, sticker, center stack,
  modular grid, magazine cover, corner minimal, sandwich (word behind subject).
  The idea follows the material: no photo → type-led ideas; one short word →
  giant type; product cut-out → sticker or depth sandwich.

## 6. Photos

- **One focal subject.** Crop to the subject; set the focus point on the face
  or product. Cover-fit for framed photos, contain-fit for cut-outs so the
  subject is shown whole.
- **Photos never cover text.** *(check: covered_text)* When text must sit on a
  photo, add a fade, a solid panel, or pick a calm area of the photo.
- **Cut out only what cuts cleanly.** A sticker cut-out works for one subject
  on a background (a product, a pet, a person from the waist up). A tiny subject
  in a wide scene, several separate people, or a subject the frame already crops
  at the top or sides looks broken as a cut-out: frame it instead. *(automatic:
  `cutout_suitability` in `image_fx.py`; the composer then frames the photo and
  skips cut-out-only ideas)*
- **Cut-outs create depth.** A cut-out subject in front of a giant word (word
  behind the head) adds depth cheaply. Add an outline or a soft shadow so it
  doesn't look pasted.
- **Treatment matches the look.** Duotone, grayscale, halftone, or grain tie
  a photo into the palette; one treatment per graphic.
- **Rights first.** Commercial rights for every photo, font, and texture.

## 7. Depth and texture

- **Layers:** background → decoration → photo → text → foreground accents.
  Text behind a subject is allowed only for a giant decorative word that
  stays legible, never for the message itself.
- **Texture is seasoning.** Grain, scanlines, smoke, and paper sit over
  everything at low opacity (≈0.03–0.1 for grain). They must not reduce the
  contrast of real text.
- **Decoration goes to the edges.** Motifs belong in corners and margins or
  behind panels. The reading area stays calm.

## 8. Formats and safe zones

| Format | Size | Notes |
|---|---|---|
| square | 1080×1080 | Feed. Centered or grid layouts work. |
| portrait | 1080×1350 | Feed, takes the most screen. Prefer it for feed posts. |
| story | 1080×1920 | Keep text out of the top ~14% and bottom ~20% (app UI). |
| landscape | 1200×630 | Link previews, banners. Short copy only. |

- Each size gets its own arrangement; do not scale a square into a story.
- Print: 300 dpi, `export --scale 3 --dpi 300`, keep 3 mm bleed when the
  printer asks for it.

## 9. Series and variety

- **Same family, different faces.** In a campaign, hold palette, type, logo
  position, and photo treatment constant. Vary the composition idea, crop,
  hero, and accent placement per post. *(check: near-copy memory, similarity
  ≥ 0.8 rejected)*
- **Never paste the last job's layout.** Every job gets a composition designed
  from its own material; the layout library remembers delivered layouts so new
  ones differ.
- **Variety has limits.** A feed that changes everything every post looks like
  five brands. Change one or two big things per post, not all of them.

## 10. Brand and ethics

- **Logo:** one per graphic, in a corner, about 7% of the short side tall, with
  clear space of ~40% of its height that no text enters; the same corner across
  a campaign. When a quarter or more of the logo would vanish into the
  background (or it sits on a photo), it gets a small white or near-black plate.
  Never stretched or recolored outside the brand rules. *(automatic: `--logo`,
  `logo_position`; checks `logo_crowded`, `logo_covered`)*
- No imitation of another brand's identity, no protected emblems, no fake
  reviews, prices, or claims the client cannot prove.
- Accessibility: contrast, readable sizes, and alt text when posting.
