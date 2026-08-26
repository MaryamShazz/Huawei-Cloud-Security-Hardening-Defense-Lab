# Cloud Trace Service Logging Coverage

| Service | Logged | Notes |
|---|---|---|
| IAM | Yes | User, group, and policy changes |
| VPC | Yes | Subnet and route table changes |
| Security Groups | Yes | Rule additions/removals |
| Cloud Firewall | Yes | Policy changes |
| Object Storage | Yes | Bucket policy and access changes |
| ECS | Yes | Instance start/stop/terminate, config changes |

Retention: 365 days. Log destination bucket is not writable or deletable by the accounts being audited — see [`cts-config-template.json`](cts-config-template.json).
