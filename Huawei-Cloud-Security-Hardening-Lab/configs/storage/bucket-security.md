# Object Storage Bucket Security Summary

| Setting | Value | Reason |
|---|---|---|
| Public access | Disabled by default | Prevents accidental data exposure |
| Server-side encryption | Enabled | Protects data at rest |
| Versioning | Enabled | Protects against accidental delete/overwrite |
| External sharing method | Signed URL with expiry | Avoids making the bucket itself public |

No actual bucket names, account IDs, or endpoint URLs are recorded here, this is a settings summary, not a live configuration export.
