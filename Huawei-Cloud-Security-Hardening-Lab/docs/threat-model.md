# Threat Model

This sits ahead of the risk assessment in `risk/risk-assessment.md` and answers a narrower question: for each asset in this environment, what's the realistic threat, where's the attack surface, and what control is already in place to address it. The risk assessment then rates and prioritizes what's listed here.

## Methodology

The model follows a simple chain for each asset: **Asset → Threat → Attack Surface → Existing Control → Validation**. Validation is tracked separately in `validation/validation-results.md` rather than duplicated here, so this document stays focused on identifying the threat rather than proving the control works.

## Asset / Threat Matrix

| Asset | Threat | Attack Surface | Existing Control |
|---|---|---|---|
| IAM accounts | Credential compromise | Console / API login | MFA + group-based least privilege |
| Bastion host | Brute-force login attempts | SSH (port 22) | Source IP restriction, no open internet access |
| ECS instances | Unauthorized access / lateral movement | Internal network | Private subnet, no public IP, tiered security groups |
| Object Storage (OBS) | Data exposure via misconfigured bucket | Storage API / public URL | Private-by-default buckets, encryption, signed URLs |
| Cloud configuration | Malicious or accidental change | Management APIs | Cloud Trace Service (CTS) audit logging |
| Infrastructure (compute) | Resource compromise, cryptomining, DoS | Runtime / instance level | Cloud Eye monitoring and alert thresholds |
| Backups / snapshots | Data loss, unrecoverable state | Backup service | Scheduled snapshots, tested restore |
| Network boundary | External scanning, exploitation attempts | Internet-facing edge | Cloud Firewall allow/deny lists |

## Why each asset is in scope

**IAM accounts** are the entry point for every other control in this environment. If an account is compromised, the attacker inherits whatever that account's group permissions allow, which is why the account layer gets its own row rather than being folded into "network."

**The bastion host** is the only resource in the environment with a public IP, which makes it the single most exposed asset and the most likely target for automated scanning and brute-force attempts.

**ECS instances** sit behind the bastion and the private subnet, but they're still a target once an attacker has any foothold on the internal network, whether through the bastion or through a misconfigured security group.

**Object storage** is included because bucket misconfiguration (accidentally public buckets) is one of the most common real-world cloud data exposure incidents, independent of how well the network layer is secured.

**Cloud configuration itself** is treated as an asset because a malicious or accidental change to a security group, firewall rule, or IAM policy can silently undo every other control on this list. This is why CTS logging is treated as a control against configuration-layer threats specifically, not just a general audit nicety.

**Infrastructure at runtime** covers the case where a resource is compromised after the fact, e.g. a dependency vulnerability or a leaked credential used for lateral movement, which is why Cloud Eye is listed as a detective control here rather than purely a performance tool.

**Backups** are their own asset because ransomware-style scenarios and accidental deletion both depend on backups being intact and restorable, not just scheduled.

**The network boundary** is listed separately from the bastion and ECS rows because Cloud Firewall protects against threats that never make it past the edge at all, before they reach any specific host.

## Relationship to other documents

- Ratings (impact, likelihood, residual risk) for the threats above live in [`risk/risk-assessment.md`](../risk/risk-assessment.md).
- Ongoing residual risk that can't be fully closed off is tracked in [`risk/residual-risk-register.md`](../risk/residual-risk-register.md).
- Evidence that each control listed here actually works as intended is in [`validation/validation-results.md`](../validation/validation-results.md).
