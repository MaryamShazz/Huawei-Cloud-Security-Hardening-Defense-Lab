# ADR-003: Default-Deny Security Groups Instead of Default-Allow with Exceptions

## Decision
Every security group in this environment starts from default-deny, with rules added explicitly for what's actually needed, rather than starting permissive and removing access afterward.

## Why
Starting permissive and trimming later depends on someone actually coming back to do the trimming, which is exactly the kind of step that gets skipped under time pressure. Default-deny means anything not explicitly allowed is already blocked from day one.

## Alternatives Considered
- **Default-allow with a cleanup pass planned after launch:** rejected, since the cleanup pass has no hard deadline and is easy to deprioritize once the environment is "working."
- **Per-instance manual firewall rules instead of security groups:** rejected as harder to maintain consistently across the tiered architecture used here.

## Security Impact
Ensures no port or protocol is reachable unless there's a specific, identifiable reason for it — directly reducing the chance of an unnoticed open administrative or database port, which is one of the most common findings in real-world cloud reviews.
