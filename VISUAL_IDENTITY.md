# Visual Identity: Neon Horizon (Light Operational Cyberpunk)

## Intent
Create a distinct light-first visual identity that feels futuristic, technical, cinematic, and custom without becoming dark-mode heavy.
The direction combines a bright editorial website with retro-anime operational UI: holographic overlays, diagnostic grids, measurement rails, command labels, and engineered surfaces.

The site should feel like a personal writing interface projected over a future workstation, not like a generic SaaS page and not like a full emergency command terminal.

## Brand Keywords
- Precise
- Futuristic
- Technical
- Energetic
- Editorial
- Operational
- Cinematic

## Design Principles
1. Light by default: bright canvas, dark text, strong contrast.
2. Cyberpunk as interface grammar, not decoration: grids, rails, labels, and telemetry should imply an operating system.
3. Neon as signal, not wallpaper: use cyan, magenta, amber, and green as controlled status accents.
4. Readability first: generous line height, restrained motion, clear hierarchy.
5. Structured surfaces: cards, borders, HUD frames, and technical panels should feel engineered.
6. Reusable system: styles are token-based and component-oriented.

## Reference Language
The visual reference is retro-anime operational UI: diagnostic screens, command overlays, biological maps, waveform displays, emergency panels, and CRT-like system readouts.

Characteristic traits:
- Black or dark panels used as contained contrast zones, not as the whole site background.
- Condensed uppercase labels with strong hierarchy: tiny diagnostic text beside oversized status words.
- Orange/red for alerts, commands, labels, and measurement marks.
- Mint/green for system data, checks, and online states.
- Cyan/blue/violet/magenta for waveforms, topology, maps, and scientific overlays.
- Measurement systems: rulers, tick marks, crosshairs, coordinates, scan lines, numbered axes.
- Geometric overlays: hex grids, contour lines, body maps, waveform graphs, circuit routing, and modular boxes.
- Flat vector forms softened by subtle analog texture: scanlines, glow, slight blur, and display noise.
- Asymmetry and partial views: panels can feel cropped, live, or mid-scan rather than perfectly centered.

Use these traits as inspiration for layout and interaction. Do not copy exact franchise terms, logos, screenshots, or copyrighted UI compositions.

## Color System
- `--theme`: near-white blue-tinted base.
- `--entry`: white cards and content surfaces.
- `--primary`: deep ink text.
- `--secondary`: muted steel text.
- `--border`: cool blue-gray separators.
- `--accent-cyan`: primary interface glow, rails, active borders.
- `--accent-magenta`: secondary energy, hover shadows, emphasis.
- `--accent-amber`: warning/status labels and command chips.
- `--accent-lime`: rare online/OK diagnostic signal.

Color balance:
- The global page stays light and editorial.
- Dark panels are reserved for hero overlays, code blocks, and high-contrast diagnostic moments.
- Amber/orange should appear as high-signal UI language, not as a full-page theme.
- Avoid letting cyan/magenta gradients become generic decorative blobs.

## Typography
- Headline font: `Orbitron` for display moments (hero, page titles, section labels).
- Body/UI font: `Space Grotesk` for post readability and UI controls.
- Mono/system font: `IBM Plex Mono` for code, coordinates, diagnostics, and small operational labels.
- Body copy remains clean and comfortable; display typography is used selectively.
- Uppercase micro-labels should be compact and purposeful. Use them to label panels and states, not to explain the website.

## Component Language
- Header/navigation: translucent command bar with precise borders, active rails, notches, and non-pill control tabs.
- Homepage hero: cinematic workstation image with HUD framing, internal rails, and a dark translucent shell panel.
- Cards (`post-entry`, books): bright engineered surfaces with accent rails, small status chips, and hard neon hover shadows.
- Buttons: crisp command controls with corner marks, gradient signal, and clear focus/hover states.
- TOC and utility boxes: structured side panels with accent rail and compact index label.
- Post content: editorial by default, with H2 markers, callout-style blockquotes, dark code blocks, and measured tables.

## Atmosphere and Motion
- Background uses CSS-generated technical atmosphere: layered grids, diagonal construction lines, scan texture, and viewport rails.
- Raster imagery is used for cinematic moments such as the homepage hero, not as a full-page wallpaper.
- Motion is short and purposeful (entry reveal + hover elevation).
- Respect reduced-motion preferences.

## Content Styling Rules
- Keep intros short and scannable.
- Use callouts/cards for key insights and references.
- Keep visual density controlled: avoid stacking too many accent elements in one viewport.
- Long-form reading always wins over theme density.
- Avoid fake interface labels that do not map to a component role.

## What To Avoid
- Full dark-mode cyberpunk as the default site surface.
- Generic SaaS pills, soft blobs, oversized rounded cards, and decorative gradients without structure.
- Overusing emergency labels until every component feels equally urgent.
- Dense terminal UI for normal prose.
- Exact visual copies of anime screenshots, terms, logos, or proprietary UI layouts.
- Heavy raster backgrounds behind article content.

## Implementation Priorities
1. Keep the light base and editorial readability.
2. Make navigation and controls feel like command tabs instead of generic buttons.
3. Use CSS for crisp global grids, scanlines, rails, and technical structure.
4. Use hero imagery for cinematic context.
5. Add operational labels only where they clarify component hierarchy.
6. Tune mobile layouts to remove decorative density before readability suffers.

## Implementation Map
- `layouts/partials/extend_head.html`: typography loading.
- `assets/css/extended/custom.css`: design tokens and component styles.
- `hugo.yaml`: force light default theme for consistent UX.
