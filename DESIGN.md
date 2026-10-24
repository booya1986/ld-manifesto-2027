# L&D Manifesto 2027, design system

The living design reference for `index.html`. Update it when a decision changes; the page must match this file.

## Intent
A printed manifesto, read like a professional article. Avi's voice comes first and loudest; the research is a second, quieter register that agrees or disagrees with him line by line; what he actually does is a third, muted register. The reader should always know which voice is speaking.

## Order of the page
1. Cover: kicker, H1, lede, byline, collage cover image.
2. **What I say** (Avi asked for this to open the page): the eleven theses as large numbered declarations, plus the pace bet, each linking to its section.
3. Bento infographic: 177 verified sources with a stacked bar by type and the 14 numbers that failed, 11 theses as verdict squares, the 2 bets, and three specimen tiles for the voices (replaces the old counters and legend).
4. (legend is now inside the bento).
5. Agreement map: one row per thesis, a dot in "agrees / qualifies / disagrees".
6. Eleven theses, each: number + statement + stamp, my voice, collage (5 of them), research with + / − / ? lines and an animated data visualization, practice, "after the research" box (original struck through, refined statement).
7. Pace bet + scorecard, closing, call to action, sources.

## Color
Paper `#f3efe6` (dark `#141311`), ink `#151413`, red `#e5322d` (dark `#ff5a4f`). Red means "the research disagrees / the weaker result / my contrarian bet". Neutral bars `--bar-base` are context ("before", comparison). Never a second accent. Both themes are tokenized on `:root`.

## Type
Display: Secular One (theses, numbers, labels of voices). Body: Heebo. Numbers use tabular figures. Signed numbers in RTL carry a left-to-right mark (U+200E) so the minus stays in front. Hebrew prefixes before Latin or digits use a non-breaking hyphen (U+2011) so "ו‑AI" never splits across lines.

## Voices
| Voice | Treatment |
|---|---|
| My voice | 1.2rem, 6px ink rule on the start side, first person |
| Research | red top rule, red label, list lines marked + (supports, ink), − (contradicts, red), ? (no evidence, muted) |
| Practice | muted text, hairline top rule |
| After the research | tinted torn-paper box; "התחלתי מ" struck through in red, refined statement in display type |

Stamps: ink fill = agrees, ink outline = qualifies, red fill = disagrees.

## Data visualizations
Every number in the research is drawn, not just written. Components: before/after pairs, bars, ring, waffle (26 of 397), pictogram people, span column chart with a hatched red "my bet" column, range band, stat tiles, month strip. Rules from the dataviz skill: one scale per chart (mixed units go into separate panels or tiles), direct labels, source under every chart, text in ink tokens.

## Motion (Emil Kowalski rules)
Animations run once when a visualization scrolls into view (IntersectionObserver, `.in`). Only transform, opacity, clip and stroke animate. Ease `cubic-bezier(0.23,1,0.32,1)`, about 1s for explanatory charts, stagger 55 to 120ms. Bars grow from the RTL start (`transform-origin:right`). `prefers-reduced-motion` shows the final state. Without JavaScript everything is visible at rest.

## Images
Higgsfield `gpt_image_2_5`, high, 2k: a constructivist propaganda poster mixed with photo collage, halftone black and white cut-outs, torn paper, red and black geometric shapes, warm paper texture, **no text in the image**. Avi rejected hand-drawn doodles for this piece ("professional"). Files in `assets/` (cover, t1, t2, t5, t7, t9, og 1200×630). Raw PNGs are not kept in the repo.

## Do not
No colons or em dashes as punctuation in Hebrew prose. No content in the page that is not in the vault manifesto note or the verified research note. No bank-internal numbers. No mixed units on one axis.

## Preview
`python3 -m http.server 8765 --directory ~/Documents/projects/ld-manifesto-2027`, then open http://localhost:8765. Stop the server when done.
