# Control Matrix

This is the same control to objective mapping introduced in [`docs/security-controls.md`](../docs/security-controls.md), kept here as well since `validation/` is where evidence facing artifacts live. If you're only looking for one copy, `docs/security-controls.md` is the canonical version; this one exists so the matrix and the validation results sit next to each other.

*No live Huawei Cloud environment has been deployed yet.* The "Validation Status" column reflects that: every control is designed and its test procedure is written, but none have been executed against a real account.

| Domain | Control | Security Objective | Evidence (once captured) | Validation Status |
|---|---|---|---|---|
| IAM | MFA on all console accounts | Account protection | `evidence/IAM/EV-IAM-01-mfa-enforcement.md` | Designed — pending deployment |
| IAM | Group-based permission assignment | Least privilege | `evidence/IAM/EV-IAM-02-group-scoped-permissions.md` | Designed — pending deployment |
| VPC | Public/private subnet split | Reduce attack surface | `evidence/VPC/EV-VPC-01-private-subnet-routing.md` | Designed — pending deployment |
| Security Groups | Default-deny, tiered rules | Restrict lateral movement | `evidence/Security-Groups/EV-SG-01-tiered-enforcement.md` | Designed — pending deployment |
| Cloud Firewall | Allow/deny lists at the network edge | Perimeter filtering | `evidence/Firewall/EV-FW-01-edge-enforcement.md` | Designed — pending deployment |
| Object Storage | Private-by-default, encryption, versioning | Data protection | `evidence/OBS/EV-OBS-01-private-bucket.md` | Designed — pending deployment |
| Cloud Trace Service | Account-wide audit logging | Accountability | `evidence/CTS/EV-CTS-01-admin-action-logging.md` | Designed — pending deployment |
| Cloud Eye | Threshold-based alerting | Detection | `evidence/Cloud-Eye/EV-CE-01-threshold-alert.md` | Designed — pending deployment |
| Cloud Backup | Scheduled snapshots, tested restore | Recovery | `evidence/Backup/EV-BK-01-restore-test.md` | Designed — pending deployment |
| Incident Response | Documented compromise scenario | Preparedness | `docs/incident-response.md` | Designed only — tabletop not scheduled |

Full test-by-test detail for each row is in [`validation/validation-results.md`](validation-results.md); the single source of truth for actual execution status is [`validation/test-register.md`](test-register.md).

## Reading this table

A row with a filled in evidence path doesn't mean the evidence file contains real data yet, every file under `evidence/` is currently a template with an "Observed Result" field marked `pending real evidence capture`. This table records where that evidence will live once a live account exists, not that it already does.
