# ADR-004: Object Storage Buckets Private by Default

## Decision
All Object Storage Service buckets are configured private by default, with encryption and versioning enabled. External sharing uses signed URLs with an expiry rather than making a bucket public.

## Why
Public storage exposure is overwhelmingly the result of a default that was never changed, not a deliberate choice. Making private the default removes that failure mode entirely rather than relying on someone remembering to set it correctly every time.

## Alternatives Considered
- **Public buckets with access controlled at the object level:** rejected — a single misconfigured object-level policy would expose data by default rather than requiring an explicit action to expose it.
- **Manual review of every bucket before launch instead of a private-by-default policy:** rejected as a process that doesn't scale and depends on a human catching every exception.

## Security Impact
Removes the most common cloud storage misconfiguration category by making exposure something that has to be deliberately configured, with a documented reason, rather than something that happens by omission.
