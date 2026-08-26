# Implementation Detail — Object Storage Security

1. Create the bucket with public access disabled at creation, not disabled afterward.
2. Enable server-side encryption on the bucket.
3. Enable versioning.
4. For any object that must be shared externally, generate a signed URL with an expiry rather than adjusting the bucket's public access setting.
5. Periodically review bucket policies for any accidentally introduced public grant.

Reference: [`configs/storage/bucket-security.md`](../../configs/storage/bucket-security.md).
