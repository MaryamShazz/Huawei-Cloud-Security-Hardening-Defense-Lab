# 01 — Identity & Access Management

## Objective
Control who can act in this environment and what they're allowed to do, before anything else is built on top of it.

## Why It Matters
Every other control in this repository assumes identity is already trustworthy. A firewall rule or a private bucket doesn't mean much if an over-permissioned or unprotected account can just reconfigure it.

## Configuration
- Groups created by function: developers, operators, auditors — not per-user policies
- MFA enforced on all console accounts
- Password policy: 12-character minimum, complexity required, 90-day rotation, lockout after 5 failed attempts
- Permission matrix reviewed against each group's actual job function

See [`configs/iam/`](../../configs/iam/) for policy and password templates.

## Screenshots
See [`screenshots/iam/`](../../screenshots/iam/).

## Security Benefit
Limits the blast radius of a single compromised credential and removes standing broad access that isn't tied to an actual role.

## Best Practices
Least privilege by group, not by individual exception. MFA on everything with console access, no "internal account" carve-outs.

## Security Engineer's Notes
It's tempting to grant broad access "just to move faster" during setup and trim it later. In practice that trimming rarely happens on schedule — reviewing the permission matrix before go-live is cheaper than reviewing it after an incident.

## Further Detail
Step-by-step implementation notes: [`implementation.md`](implementation.md), permission matrix: [`permission-matrix.md`](permission-matrix.md). Screenshots: [`screenshots/`](screenshots/).
