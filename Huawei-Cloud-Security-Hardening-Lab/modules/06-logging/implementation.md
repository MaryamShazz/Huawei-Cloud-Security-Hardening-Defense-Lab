# Implementation Detail — Logging (Cloud Trace Service)

1. Enable a system tracker in Cloud Trace Service, scoped account-wide.
2. Confirm the tracker's log targets include IAM, VPC, security groups, Cloud Firewall, OBS, and ECS actions.
3. Set the log destination bucket to disallow deletes and writes from any account other than the CTS service itself.
4. Set a retention period appropriate to the audit and investigation needs of the environment (365 days used here as a baseline).
5. Perform one test change (e.g. a security group rule edit) and confirm it appears in the log with actor, action, and timestamp.

Reference: [`configs/logging/logging-coverage.md`](../../configs/logging/logging-coverage.md) and [`configs/logging/cts-config-template.json`](../../configs/logging/cts-config-template.json).
