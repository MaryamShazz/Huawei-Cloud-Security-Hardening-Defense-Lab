# 05 — Object Storage Security

## Objective
Keep data at rest private, encrypted, and recoverable by default.

## Why It Matters
Publicly exposed storage buckets are one of the most common real-world cloud data exposure incidents, usually caused by a default that was never changed rather than a deliberate decision.

## Configuration
- Buckets private by default
- Server-side encryption enabled
- Versioning enabled
- Signed URLs with expiry used for any necessary external sharing

## Screenshots
See [`screenshots/storage/`](../../screenshots/storage/).

## Security Benefit
Limits accidental or malicious data exposure and protects against unrecoverable accidental deletion or overwrite.

## Best Practices
Any public bucket access should require an explicit, documented reason — never a default.

## Security Engineer's Notes
Versioning is one of the cheapest controls on this entire list relative to what it protects against. It's easy to skip during setup and expensive to have skipped after the fact.

## Further Detail
Step-by-step implementation notes: [`implementation.md`](implementation.md). Screenshots: [`screenshots/`](screenshots/).
