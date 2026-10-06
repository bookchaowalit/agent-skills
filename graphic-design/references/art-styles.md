# Art Styles: What Makes a Look Recognisable

A look is made of five levers moved together: **palette**, **type**,
**texture**, **motifs**, and **photo treatment**. Changing only the palette
gives a recolor, not a style. A believable style moves at least three levers in
the same direction. The engine's style packs (`graphic-art-style.v1`, list with
`book-production graphics styles`) encode exactly these levers; a new look can be
designed from a description with `style-create` (AI, needs live approval).

## Choosing a look

1. Start from the audience and the feeling, not from a style name: who is it
   for, and what should they feel (excited, calm, trusting, nostalgic, edgy)?
2. Match the feeling to a family below; check that the brand colors can live
   in it (as accent or as the main palette).
3. Look at the copy: long Thai copy needs a calm, readable look (minimal, swiss,
   luxury, handmade); one punchy word can carry a loud look (pop art, dystopia,
   arcade).
4. Keep the look for the whole series; vary the composition.

## Style vocabulary (built-in packs)

| Look | Feeling / use | Palette | Type | Texture & motifs | Photo |
|---|---|---|---|---|---|
| minimal | calm, premium, clinics, studios | off-white, black, one quiet accent | clean sans, lots of space | one thin rule; decoration removed | none |
| swiss | rational, modern, events, tech | off-white, black, signal red | tight bold sans, grid | one hard geometric shape | grayscale |
| luxury | premium, jewelry, hotels | ivory, ink, bronze | Thai serif, airy tracking (Latin only) | hairline frame | none |
| retro | warm nostalgia, cafés, food | cream, burnt orange, teal | rounded bold display | sunset arcs, stripes, soft grain | vintage |
| jazz | night, music, bars | midnight navy, brass gold, brick red | deco lettering, typewriter labels | fan arcs, notes, smoky vignette, grain | duotone |
| art_deco | glamour, gala, gold | black and brass | deco caps | rays, fan arcs, stepped frame | duotone |
| noir | drama, mystery, film | black/white + one blood red | serif, typewriter | venetian-blind stripes, heavy vignette, grain | high contrast |
| dystopia | protest, warning, gaming | concrete black, hazard yellow, red | condensed propaganda caps, mono | hazard stripes, barcode, glitch, scanlines, distress | high contrast |
| cyberpunk | tech, night city, gaming | deep indigo, neon magenta, cyan | techno sans, mono | glitch bars, HUD corners, scanlines | duotone |
| vaporwave | 80s/90s internet nostalgia | purple dusk, hot pink, cyan | wide display, pixel labels | neon grid floor, glow, scanlines | duotone |
| y2k | playful tech, fashion, youth | icy periwinkle, violet, hot pink | techno sans | sparkles, bubbles, glow, rings | none |
| arcade_8bit | games, kids, fun promos | navy night, neon pink, cyan | pixel font | checker floor, starfield, scanlines | posterize |
| pop_art | loud sale, comic, fun | yellow, red, blue, black outline | heavy display | rays, halftone, hard offset shadow | halftone |
| memphis | playful 80s, kids, events | cream, candy pink, cobalt, yellow | geometric display | squiggles, triangles, dots, zigzag | none |
| kawaii | cute, desserts, pets, kids | soft pink, mint | round hand-drawn Thai | polka dots, sparkles, blobs, sticker photos | none |
| handmade | craft, local, organic | kraft paper, ink brown, rust, green | handwritten Thai | torn paper, squiggles, grain | vintage |
| grunge | music, street, raw | charcoal, rust, bone | condensed display, typewriter | torn edges, ink splats, heavy grain | high contrast |
| risograph | indie, zines, art events | cream paper, blue, fluorescent pink | friendly sans | halftone, blobs, rough grain | duotone |

## Creating a new look from a description

- Collect the evidence words (Thai and English) people would use for it.
- Pick the palette first, then check contrast for every text role
  (ink on bg 4.5:1, on_accent on accent 3:1).
- Pick one display face with character and a quiet body face; check that
  both render Thai.
- Choose at most 2–3 motifs and one texture; keep them at the edges or faint.
- Choose one photo treatment that pulls photos into the palette.
- Test the look on at least three different compositions (with photo, type
  only, long copy) before calling it done.

## Mixing looks

Mix by lever, not by stacking: e.g. "retro palette + swiss grid" is a
deliberate mix; "retro + cyberpunk + kawaii motifs together" is noise. When
in doubt, keep one look and push one lever further.
