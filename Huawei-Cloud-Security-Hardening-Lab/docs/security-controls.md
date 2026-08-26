# Security Control Matrix

Where the threat model asks "what could go wrong," this maps each control actually implemented back to the security objective it serves and the evidence that it's in place. This is what turns the project from configuration documentation into something closer to a security assessment.

| Domain | Control | Security Objective | Evidence |
|---|---|---|---|
| IAM | MFA on all console accounts | Account protection | `screenshots/iam/` + validation result IAM-01 |
| IAM | Group-based permission assignment | Least privilege | Permission matrix, `checklists/cloud-hardening.md` |
| VPC | Public/private subnet split | Reduce attack surface | Route table review, `docs/architecture.md` |
| Security Groups | Default-deny, tiered rules | Restrict lateral movement | Rule set in `configs/security-groups/` |
| Cloud Firewall | Allow/deny lists at the network edge | Perimeter filtering | Rule set in `configs/firewall/` |
| Object Storage | Private-by-default, encryption, versioning | Data protection | Bucket configuration, `configs/` (template) |
| Cloud Trace Service | Account-wide audit logging | Accountability | Log configuration, `screenshots/logging/` |
| Cloud Eye | Threshold-based alerting | Detection | Monitoring dashboard, `screenshots/monitoring/` |
| Cloud Backup | Scheduled snapshots, tested restore | Recovery | Restore evidence, `validation/validation-results.md` |

## How this differs from the risk table

`risk/risk-assessment.md` rates the likelihood and impact of a risk occurring. This matrix instead confirms, control by control, that the thing meant to reduce that risk is actually configured and has evidence behind it. A risk can be rated "Low" in the risk table and still need its row here, since the low rating usually depends on the control in this matrix being real and not just assumed.

## Reading this table

Every row should be traceable to something concrete: a config file, a screenshot, or a validation test result. A control with no evidence column filled in is a gap, not a finished item, regardless of what the risk table says about it.
