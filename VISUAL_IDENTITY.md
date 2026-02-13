# Visual Identity: Neon Horizon (Light Cyberpunk)

## Intent
Create a distinct light-first visual identity that feels futuristic, technical, and cinematic without becoming dark-mode heavy.
The direction is inspired by retro-future city aesthetics (neon signage, holographic overlays, engineered surfaces) while preserving high readability for long-form writing.

## Brand Keywords
- Precise
- Futuristic
- Technical
- Energetic
- Editorial

## Design Principles
1. Light by default: bright canvas, dark text, strong contrast.
2. Neon as accent, not background: use cyan/magenta as controlled highlights.
3. Structured surfaces: cards, borders, and subtle grid atmosphere.
4. Readability first: generous line height, restrained motion, clear hierarchy.
5. Reusable system: styles are token-based and component-oriented.

## Color System
- `--theme`: near-white blue-tinted base.
- `--entry`: white cards and content surfaces.
- `--primary`: deep ink text.
- `--secondary`: muted steel text.
- `--border`: cool blue-gray separators.
- `--accent-cyan`: primary neon highlight.
- `--accent-magenta`: secondary neon highlight.
- `--accent-amber`: warm counter-accent for small emphasis.

## Typography
- Headline font: `Orbitron` for display moments (hero, page titles, section labels).
- Body/UI font: `Space Grotesk` for post readability and UI controls.
- Body copy remains clean and comfortable; display typography is used selectively.

## Component Language
- Header/navigation: translucent light panel with precise borders and subtle blur.
- Cards (`post-entry`, books): bright surfaces, elevated shadows, neon hover edge.
- Buttons: gradient accent with crisp shape and defined interaction state.
- TOC and utility boxes: structured side panels with accent rail.

## Atmosphere and Motion
- Background uses layered gradients and a faint technical grid texture.
- Motion is short and purposeful (entry reveal + hover elevation).
- Respect reduced-motion preferences.

## Content Styling Rules
- Keep intros short and scannable.
- Use callouts/cards for key insights and references.
- Keep visual density controlled: avoid stacking too many accent elements in one viewport.

## Implementation Map
- `layouts/partials/extend_head.html`: typography loading.
- `assets/css/extended/custom.css`: design tokens and component styles.
- `hugo.yaml`: force light default theme for consistent UX.

