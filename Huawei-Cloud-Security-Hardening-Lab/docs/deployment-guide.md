# Deployment Guide

This is the actual build order, matching the module numbering used throughout the repository (`modules/01-iam` through `modules/09-infrastructure-hardening`, followed by risk, validation, and incident response). Each step assumes the previous one is already in place.

```
01  IAM foundation
      │
      ▼
02  VPC + subnets (public / private)
      │
      ▼
03  Bastion deployed (public subnet)
      │
      ▼
04  ECS workload deployed (private subnet)
      │
      ▼
05  Security Groups applied (tiered: bastion / app / db)
      │
      ▼
06  Cloud Firewall configured (edge allow/deny)
      │
      ▼
07  Object Storage secured (private, encrypted, versioned)
      │
      ▼
08  Cloud Trace Service (CTS) enabled
      │
      ▼
09  Cloud Eye configured (monitoring + alerts)
      │
      ▼
10  Cloud Backup configured (snapshots + restore test)
      │
      ▼
11  Infrastructure hardening pass (checklist run against live environment)
      │
      ▼
12  Risk Assessment + Threat Model reviewed
      │
      ▼
13  Security Validation (control matrix + evidence)
```

Note on numbering: the nine **modules** (`modules/01-iam` … `modules/09-infrastructure-hardening`) map to build steps 01, 02+03 combined, 05, 06, 07, 08, 09, 10, 11 above — network setup spans two module folders (VPC and Security Groups) but three build steps (VPC, bastion, ECS), since the bastion and the workload are deployed at different points even though they both belong to the network security domain. Steps 12–13 (risk assessment and validation) aren't separate modules; they're the review layer that runs across every module, tracked in `risk/` and `validation/` instead.

## 01. IAM Foundation

- Create an admin group and scoped groups (developers, operators, auditors) instead of assigning permissions per user.
- Attach policies to groups, not individual accounts.
- Enforce MFA on every account with console access.
- Set the account password policy: minimum length, rotation period, lockout threshold.
- Review the permission matrix before moving on; trim anything broader than the role requires.

Full detail: [`modules/01-iam/`](../modules/01-iam/README.md)

## 02. VPC and Subnets

- Create the VPC and define the CIDR range.
- Split into a public subnet and a private subnet.
- Attach the Internet Gateway only to the public subnet's route table.
- Configure NAT so private subnet instances get outbound-only internet access.
- Confirm the private subnet's route table has no direct path to the Internet Gateway.

Full detail: [`modules/02-vpc-network-security/`](../modules/02-vpc-network-security/README.md)

## 03–04. Bastion and ECS Workload

- Deploy the bastion host in the public subnet; this is the only resource in the environment with a public IP.
- Deploy the ECS instances running the application in the private subnet, with no public IP.
- Confirm the only path from the bastion to the workload is over the internal network.

## 05. Security Groups

- Bastion security group: inbound SSH restricted to known source IPs.
- Application tier security group: inbound limited to the bastion and the load balancer tier.
- Database tier security group: inbound limited to the application tier on the database port only.
- Test connectivity from each tier to confirm nothing is over-permissioned.

Full detail: [`modules/03-security-groups/`](../modules/03-security-groups/README.md)

## 06. Cloud Firewall

- Define an allow list matching expected traffic.
- Define a deny list for known-bad ranges.
- Test both lists against legitimate and blocked traffic before moving on.

Full detail: [`modules/04-cloud-firewall/`](../modules/04-cloud-firewall/README.md)

## 07. Object Storage Security

- Set new buckets to private by default.
- Enable server-side encryption and versioning.
- Use signed URLs with an expiry for anything that needs external sharing.

Full detail: [`modules/05-object-storage/`](../modules/05-object-storage/README.md)

## 08. Logging (Cloud Trace Service)

- Enable CTS account-wide.
- Confirm administrative actions (IAM, security group, firewall changes) are captured.
- Route logs to a destination the audited accounts can't edit or delete.

Full detail: [`modules/06-logging/`](../modules/06-logging/README.md)

## 09. Monitoring (Cloud Eye)

- Enable Cloud Eye on all ECS instances.
- Set alert thresholds based on expected baseline usage.
- Confirm alerts reach a real notification channel.

Full detail: [`modules/07-monitoring/`](../modules/07-monitoring/README.md)

## 10. Backup and Recovery

- Schedule snapshots.
- Document and actually run a test restore.

Full detail: [`modules/08-backup-recovery/`](../modules/08-backup-recovery/README.md)

## 11. Infrastructure Hardening Pass

- Run `checklists/cloud-hardening.md` against the live environment.
- Disable unused services and ports.
- Confirm instances are current on patches.

Full detail: [`modules/09-infrastructure-hardening/`](../modules/09-infrastructure-hardening/README.md)

## 12. Risk Assessment and Threat Model Review

- Confirm every asset in `docs/threat-model.md` has a corresponding control from steps 01–11.
- Rate and log risks in `risk/risk-assessment.md`.
- Log anything that can't be fully closed off in `risk/residual-risk-register.md`.

## 13. Security Validation

- Run each control against its expected result in `validation/validation-results.md`.
- Confirm the control matrix in `validation/control-matrix.md` has evidence for every row.
- Update the findings dashboard in `validation/findings-summary.md`.
- Run the final pass in `checklists/security-review.md`.

Once step 13 is complete, the environment is considered ready for the state described in `reports/baseline-security-report.md`.
