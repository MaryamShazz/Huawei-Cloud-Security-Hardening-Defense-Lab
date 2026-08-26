# 06 — Logging (Cloud Trace Service)

## Objective
Make every administrative action and API call attributable to an actor and a timestamp.

## Why It Matters
Without an audit trail, "who changed this and when" has no answer after the fact, which makes both incident response and accountability effectively impossible.

## Configuration
- Cloud Trace Service enabled account-wide
- Administrative actions (IAM, security group, firewall changes) confirmed captured
- Logs routed to a destination the audited accounts can't edit or delete

See [`configs/logging/`](../../configs/logging/) for the tracker configuration template.

## Screenshots
See [`screenshots/logging/`](../../screenshots/logging/).

## Security Benefit
Supports both detection (spotting an unexpected change) and post-incident investigation (reconstructing what happened).

## Best Practices
The log destination itself needs its own access control — a compromised account shouldn't be able to cover its tracks by editing the log that would reveal it.

## Security Engineer's Notes
Logging's value isn't felt until the first time something looks wrong and someone needs a fast, reliable answer to "who did this."

## Further Detail
Step-by-step implementation notes: [`implementation.md`](implementation.md). Screenshots: [`screenshots/`](screenshots/).
