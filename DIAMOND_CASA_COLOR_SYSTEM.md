# Diamond Casa Color System & Site Mapping

This document captures the approved Diamond Casa palette, the CSS token block to add to the main stylesheet, and a section-by-section color application map for the homepage plus general PDP guidance. It also includes a developer checklist for implementation.

## Palette

**Neutrals / backgrounds**
- Casa Ivory – `#F6F3ED`
- Casa Eggshell – `#F9F7F1`
- Casa Stone – `#E7E3DF`
- Casa Mist – `#D4CFC5` / `#C5C2B7`

**Brand greens**
- Casa Sage – `#687466`
- Casa Sage Dark – `#5D6759` / `#7A7B73`

**Soft accent**
- Casa Taupe – `#B0968F`

**Deep contrast (sparingly)**
- Casa Charcoal – `#010101`

## CSS tokens to add

```css
:root {
  --dc-bg:        #F6F3ED;  /* Casa Ivory */
  --dc-bg-alt:    #F9F7F1;  /* Eggshell */
  --dc-bg-stone:  #E7E3DF;  /* Stone */

  --dc-primary:       #687466; /* Casa Sage */
  --dc-primary-dark:  #5D6759;
  --dc-accent:        #B0968F; /* Taupe */

  --dc-border:    #D4CFC5;  /* Mist */
  --dc-border-alt:#C5C2B7;

  --dc-text-main:   #2E302B; /* warm near-black */
  --dc-text-muted:  #7A7B73;
  --dc-text-light:  #F6F3ED;

  --dc-black:     #010101;
  --dc-error:     #3B0404;  /* deep warning */
}

.btn-primary {
  background: var(--dc-primary);
  color: #fff;
  border-radius: 999px;
  padding: 10px 32px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  font-size: 11px;
}
.btn-primary:hover {
  background: var(--dc-primary-dark);
}

.btn-secondary {
  background: transparent;
  color: var(--dc-primary);
  border-radius: 999px;
  border: 1px solid var(--dc-primary);
}
.btn-secondary:hover {
  background: var(--dc-primary);
  color: #fff;
}
```

> Quick start: the tokens and section-level styling are prebuilt in `assets/css/diamond-casa-theme.css` so you can drop the stylesheet into the storefront shell and immediately pick up the approved palette, buttons, and band treatments.

## Homepage section mapping

Use the tokens above and remove legacy reds/blues/golds except where explicitly noted.

### 1) Top promo bar
- Background: `var(--dc-black)` or `var(--dc-primary-dark)` (pick one globally).
- Text: `var(--dc-bg)`; timer/code pill border & text: `var(--dc-accent)`; pill background transparent.

### 2) Header & navigation
- Header background: `var(--dc-bg)`.
- Nav links: `var(--dc-primary)`; hover/active underline or 2px bottom border: `var(--dc-primary-dark)`.
- Icons (login/cart): `var(--dc-primary)`; cart badge background: `var(--dc-accent)`, text white.

### 3) Hero tiles (e.g., "Our Most Loved Diamond Rings", "Best-Selling Earrings")
- Section background: `var(--dc-bg-alt)`.
- Headlines: `var(--dc-primary-dark)`; subtext: `var(--dc-text-muted)`.
- CTAs: `btn-primary` as defined above.

### 4) Category strip (Shop Rings / Bracelets / Necklaces / Earrings / Bangles)
- Strip background: `var(--dc-bg)`.
- Tile background: `#FFFFFF`; border: `1px solid var(--dc-border)`.
- Title: `var(--dc-primary)`.
- Hover: subtle shadow + border color `var(--dc-primary)` (no fill).

### 5) Product grids ("Everyday Elegance", etc.)
- Section background: `var(--dc-bg-alt)`.
- Card background: `#FFFFFF`; border: `1px solid var(--dc-border)`.
- Name: `var(--dc-text-main)`; price: `var(--dc-primary-dark)`.
- Dots/pagination: active `var(--dc-primary)`, inactive `var(--dc-border)`.
- Promo badges (if any): background `var(--dc-accent)`, text white.

### 6) Editorial blocks ("Beauty & Ingenuity", "Ear Stack Magic", "Wristwear Essentials")
- Band background: `var(--dc-bg)`.
- Section label: `var(--dc-accent)` small caps.
- Heading: `var(--dc-primary-dark)`; body: `var(--dc-text-muted)`.
- Buttons: `btn-primary` or `btn-secondary`.
- Place tagline "Effortless Elegance Everyday" once as subheading in `var(--dc-text-muted)`.

### 7) Engagement rings strip
- Background: `#FFFFFF` or `var(--dc-bg)`.
- Label line text: `var(--dc-primary-dark)`, letter-spacing 0.12em, all caps, small size.
- Cards: same styling as product grids; sublines in `var(--dc-text-muted)`.

### 8) Blog section ("From Our Blog")
- Section background: `var(--dc-bg-alt)`.
- Cards: `#FFFFFF` with `1px solid var(--dc-border)`.
- "News" label: `var(--dc-accent)`.
- Titles: `var(--dc-primary-dark)`; links: `var(--dc-primary)` → hover `var(--dc-primary-dark)`.

### 9) Bottom USP band ("Shipping Worldwide" etc.)
- Band background: `var(--dc-bg)`.
- Icons: `var(--dc-primary)`.
- Headings: `var(--dc-primary-dark)`; body: `var(--dc-text-muted)`.

### 10) Footer
- Background: choose **Option A** `var(--dc-primary-dark)` or **Option B** `var(--dc-black)` and keep consistent.
- Column headings: `var(--dc-text-light)` with letter-spacing, uppercase.
- Links: `#F6F3ED` at ~75% opacity; hover → full opacity + underline.
- Newsletter input: bg `rgba(246,243,237,0.08)`; border `1px solid var(--dc-border)`; text `var(--dc-text-light)`.
- Newsletter CTA: `btn-primary`; adjust text color depending on footer background (light text on dark bg).
- Bottom bar: same background, top border `rgba(213,207,197,0.35)`, text small in a light muted tone.
- Place the circular "Effortless Elegance Everyday" seal centered above newsletter or copyright.

## PDP guidelines
- Page background: `var(--dc-bg)`.
- Gallery: white background with soft borders `var(--dc-border)` only if needed.
- Product name: `var(--dc-primary-dark)`; subheading: `var(--dc-text-muted)`.
- Price: `var(--dc-primary)`; strikethrough MRP (if any): `var(--dc-text-muted)`; discount badge: background `var(--dc-accent)`, text white.
- Primary CTAs: `btn-primary`.
- Tabs: text `var(--dc-primary)`; active underline `var(--dc-primary-dark)`; background stays `var(--dc-bg)`.

## Cleanup and consistency
- Remove all test/dummy products from home (e.g., "teesttest 14KT", "Moissanite product testing 14KT", Rs 6 items).
- Replace lorem ipsum in editorial blocks with real copy.
- Newsletter line copy: "Sign up for Diamond Casa stories, styling tips & private previews.".
- Standardize CTA text to: "Shop Now", "Discover the Collection", or "Learn More".
- Ensure icons, hovers, and small accents use only `var(--dc-primary)` and `var(--dc-accent)`.

## Quick dev checklist
1. Add the CSS token block above to the main stylesheet.
2. Set `body` background to `var(--dc-bg)`, default text to `var(--dc-text-main)`, and headings to `var(--dc-primary-dark)`.
3. Search theme CSS for hard-coded bright colors and remap them to tokens.
4. Apply `btn-primary`/`btn-secondary` to all CTAs.
5. Update header, promo bar, footer, product cards, editorial blocks, and PDPs per the mapping above.
6. Remove test data, replace lorem copy, update newsletter text.
