# 08 — Backup & Recovery

## Objective
Make sure data and instance state can actually be recovered, not just backed up.

## Why It Matters
An untested backup is a plan, not a working recovery process. The difference only becomes visible at the worst possible time if it's never checked beforehand.

## Configuration
- Scheduled ECS snapshots
- Documented recovery process
- One test restore performed to a new test instance, data integrity confirmed

## Screenshots
See [`screenshots/backup/`](../../screenshots/backup/).

## Security Benefit
Provides a path back to a known-good state after data loss, accidental deletion, or a destructive incident.

## Best Practices
Test a restore under conditions closer to an actual incident, not just a clean, planned test run.

## Security Engineer's Notes
**Status: single restore test performed. Flagged in `risk/residual-risk-register.md` (RR-02) pending a second test tied to the incident response tabletop exercise.**

## Further Detail
Step-by-step implementation notes: [`implementation.md`](implementation.md), restore test record: [`restore-test.md`](restore-test.md). Screenshots: [`screenshots/`](screenshots/).
