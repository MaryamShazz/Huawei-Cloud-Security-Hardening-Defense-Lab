# 📋 Security Baseline Report (Design Stage)

| **Project Scope** | Huawei Cloud environment designed and documented in this repository |
|-------------------|---------------------------------------------------------------------|
| **Prepared By** | Me |
| **Purpose** | Document the proposed security baseline for technical review prior to deployment |
| **Current Status** | Design complete • Live deployment pending |

> *Important*
>
> No live Huawei Cloud environment has been deployed for this project.
>
> This report documents the proposed architecture, security controls, and design decisions that have been planned and reviewed. It should not be interpreted as evidence that these controls have been implemented or validated in a production cloud environment.

---

# 📖 Executive Summary

The proposed environment has been designed around established cloud security principles, including:

- Network segmentation
- Least privilege access control
- Layered network protection
- Encrypted and versioned storage
- Centralized logging
- Continuous monitoring
- Backup and recovery planning

This report summarizes the current design baseline, explains the intended security controls, and identifies which aspects remain pending implementation and validation within Huawei Cloud.

---

# 🔐 Identity & Access Management

The proposed IAM model groups users according to operational responsibilities, including developers, operators, and auditors.

The design specifies:

- Group based permission management
- Multi Factor Authentication (MFA) for all console accounts
- Password complexity requirements
- Account lockout after repeated authentication failures
- Periodic password rotation

The permission matrix documented in `modules/01-iam/permission-matrix.md` has been reviewed to ensure permissions align with each role's intended responsibilities.

> *Current Status:* Design reviewed. Live IAM configuration has not yet been deployed or validated.

---

# 🌐 Network Architecture

The proposed architecture separates the environment into public and private subnets within a single Virtual Private Cloud (VPC).

The design includes:

- Public subnet containing only a bastion host
- Private subnet hosting ECS instances
- No direct internet access for private resources
- Outbound connectivity provided through NAT for updates and package downloads

At this stage, no VPC has been provisioned. The architecture represents a reviewed design rather than an implemented cloud environment.

> *Current Status:* Architecture documented. Deployment pending.

---

# 🔥 Security Groups & Cloud Firewall

The network security model follows a default deny approach.

The proposed configuration includes:

- SSH access to the bastion host limited to approved source IP addresses
- Application servers accepting traffic only from trusted internal sources
- Database services accepting traffic only from the application tier
- Cloud Firewall providing an additional filtering layer at the network boundary

No security group rules or firewall policies have yet been created within a Huawei Cloud account.

> *Current Status:* Design complete. Configuration pending deployment.

---

# 🗄️ Object Storage

The storage design specifies that Object Storage Service (OBS) buckets should be:

- Private by default
- Encrypted at rest
- Protected with object versioning
- Shared externally only through signed URLs

No storage resources have been created at this stage.

> *Current Status:* Planned configuration only.

---

# 📈 Logging & Monitoring

The proposed monitoring strategy includes:

- Cloud Trace Service for administrative actions and API activity
- Cloud Eye monitoring for CPU, memory, storage, and network utilization
- Alert thresholds based on expected operating conditions

These services have not yet been enabled, and alert thresholds have not been validated using production workloads.

> *Current Status:* Monitoring strategy documented. Implementation pending.

---

# 💾 Backup & Recovery

The design includes scheduled backups together with a documented recovery procedure.

Recovery planning is documented in:

`modules/08-backup-recovery/restore-test.md`

Because no ECS instances have been deployed, backup and restoration procedures have not yet been executed.

> *Current Status:* Recovery plan documented. Validation pending deployment.

---

# 📊 Security Baseline Assessment

| Security Area | Status | Current Assessment |
|--------------|--------|--------------------|
| Least privilege access | 🟡 Designed | Permission model documented and reviewed |
| Multi Factor Authentication | 🟡 Designed | Required for all console accounts but not configured |
| Network segmentation | 🟡 Designed | Public and private subnet architecture documented |
| Security groups | 🟡 Designed | Default deny policy planned; rules not implemented |
| Storage protection | 🟡 Designed | Encryption and versioning specified |
| Logging | 🟡 Designed | Cloud Trace configuration documented |
| Monitoring | 🟡 Designed | Initial thresholds proposed but not validated |
| Backup & recovery | 🟡 Designed | Recovery process documented; testing pending |

---

# ✅ Conclusion

The proposed security baseline provides a complete architectural design aligned with widely accepted cloud security practices.

All security controls described in this report have been documented and reviewed as part of the design process. However, *none have yet been implemented or validated within a live Huawei Cloud environment*.

Following deployment, each security control should be reassessed through practical testing using the procedures documented in `validation/test-register.md`. At that stage, the current Designed status can be replaced with implementation results such as Pass, Partial or Not Met, based on direct observation of the deployed environment.