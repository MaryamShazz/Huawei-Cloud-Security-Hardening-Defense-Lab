# 09 — Infrastructure Hardening

## Objective
Cross-check every module above against a single hardening checklist, and close anything left over-permissive by default.

## Why It Matters
Individual modules can each be configured "correctly" and still leave a gap between them. This pass exists to catch that gap.

## Configuration
- Unused services and ports disabled
- Patch status confirmed current across all instances
- Full pass against [`checklists/cloud-hardening.md`](../../checklists/cloud-hardening.md)

## Security Benefit
Closes off opportunistic attack paths that don't depend on any single misconfiguration, just general neglect (an old open port, a service nobody uses anymore).

## Best Practices
Re-run this checklist after any major configuration change, not just once at the end of the initial build.

## Security Engineer's Notes
**Status: patch cadence flagged in `risk/residual-risk-register.md` (RR-03) — a schedule only reduces risk if it's actually followed over time, which can't be confirmed from a single pass.**

## Further Detail
Full checklist: [`hardening-checklist.md`](hardening-checklist.md) (points to `checklists/cloud-hardening.md`). Screenshots: [`screenshots/`](screenshots/).
