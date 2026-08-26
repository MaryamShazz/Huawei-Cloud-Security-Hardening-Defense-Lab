# References & Security Best-Practice Mapping

This repository doesn't claim formal compliance or certification against any standard. The mapping below shows which general security best practices each control draws on, for context, not as a certification claim.

## Security Best-Practice Mapping

| Project Control | Reference |
|---|---|
| Least privilege (IAM groups, MFA) | CIS Controls / general IAM best practices |
| Network segmentation (public/private subnets) | Cloud security architecture best practices |
| Default-deny security groups | CIS Cloud Security Benchmarks (general reference) |
| Account-wide audit logging (CTS) | Audit and security logging principles |
| Encryption at rest (OBS) | Cloud data protection best practices |
| Threshold-based monitoring (Cloud Eye) | Security monitoring and detection principles |
| Tested backup and recovery | Business continuity / disaster recovery best practices |

## What this is, and isn't

This is a **Security Best-Practice Mapping**, not a **CIS Certified Environment**. No formal audit against CIS or any other benchmark has been performed, and this repository doesn't claim one. The mapping exists to show the reasoning behind each control is grounded in recognized general practice, not invented from scratch.

## Primary references

- Huawei Cloud Identity and Access Management (IAM) documentation
- Huawei Cloud Virtual Private Cloud (VPC) documentation
- Huawei Cloud Security Group and Cloud Firewall documentation
- Huawei Cloud Trace Service (CTS) and Cloud Eye documentation
- Huawei Cloud Backup documentation
- CIS Cloud Security Benchmarks (general reference for hardening checklist structure)
- Huawei ICT Academy Cloud Security curriculum (foundational course material for this project)
