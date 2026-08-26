# Theme Style Guide — Cloud Blueprint

This repository uses a single consistent visual identity across the README, docs, and generated assets. The intent is to make it read like cloud infrastructure documentation (something closer to Cisco or Azure docs) rather than a typical open-source software README with a blue banner and dashboard screenshots.

## Color Palette

| Role | Hex | Notes |
|---|---|---|
| Background | `#0B1220` | Very dark navy, not pure black. Diagrams and text stay readable against it without looking harsh. |
| Card / Panel | `#162033` | Slightly lighter navy, used for callout boxes and card-style sections. |
| Primary Accent | `#4FD1C5` | Soft cyan. Used for headings, active elements, and primary badges. |
| Secondary Accent | `#7DD3FC` | Sky blue. Used for secondary badges and supporting diagram elements. |
| Success | `#22C55E` | Confirmed controls, passed checks. |
| Warning | `#FBBF24` | Partial controls, things flagged for follow-up. |
| Danger | `#EF4444` | Failed checks, open findings. |
| Text | `#E5E7EB` | Light gray, not pure white, for body text on dark backgrounds. |

If you're building a GitHub Pages site or a Figma mockup from this repository, these are the only colors that should appear. Avoid introducing a stray blue, red, or green outside this set, since it breaks the "single coherent document" feel.

## What to avoid

- Neon glow effects, glitch text, or binary-rain style graphics
- Hacker-in-a-hoodie or shield-with-lock stock imagery
- Red-and-black "cybersecurity" color schemes
- CI/build status badges (this is a documentation-first repository, not a CI/CD pipeline)

## Navigation and section labeling

Sections are numbered like documentation chapters (`01 Identity & Access Management`, `02 Network Architecture`, and so on) rather than plain markdown headers like `## IAM`. This is a small change but it's what makes the repository feel like a manual someone would hand to a client, instead of a list of completed exercises.

## Module layout

Every module in `docs/` and every section in the README follows the same shape, in this order:

1. Objective — what this module protects
2. Why it matters — the real-world consequence of skipping it
3. Configuration — what was actually set up
4. Screenshots — console evidence, with a caption
5. Security benefit — how this stops or slows down an attacker
6. Best practices — the general principle behind the specific config
7. Security Engineer's Notes — a short, personal note on a real-world consideration tied to that module

Keeping this order identical across every module is what makes the repository read as one document instead of eleven separate write-ups.

## Callout box conventions

Two recurring callout types appear throughout the docs:

**Security Insight** — a general principle worth remembering, usually placed right after a configuration step.

**Common Misconfiguration** — a specific mistake people make in that area, and why it's a problem.

Both are formatted as blockquotes in markdown so they visually separate from the surrounding explanation without needing custom HTML.

## Screenshot presentation

Screenshots are never dropped in on their own. Each one gets a short block: what it's a screenshot of, one line on why it matters, the image itself, and a short list of what to look for in it (MFA enabled, roles separated, and so on). This keeps the screenshots gallery from turning into an unlabeled dump of console captures.
