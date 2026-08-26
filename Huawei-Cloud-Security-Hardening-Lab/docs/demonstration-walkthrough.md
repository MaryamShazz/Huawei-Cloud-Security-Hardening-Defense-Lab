# Project Demonstration Walkthrough

This is a suggested walkthrough order for showing this project to someone else, whether that's a live screen-share, a recorded walkthrough, or just a reading order for a reviewer going through the repository on their own. It's not a video file — treat it as a script.

## 01. Architecture
Start with `docs/architecture.md` and the diagram in the README. Establish the public/private subnet split and where each service sits before getting into any individual control.

## 02. IAM Hardening
`modules/01-iam/` — groups, MFA, password policy, and the permission matrix as the visible evidence of least privilege.

## 03. Network Configuration
`modules/02-vpc-network-security/` — subnet plan and route table review, specifically pointing out the absence of a private-subnet route to the Internet Gateway.

## 04. Security Groups
`modules/03-security-groups/` — the tiered rule matrix, and test T-001/T-004 as evidence the rules actually hold.

## 05. Cloud Firewall
`modules/04-cloud-firewall/` — the boundary layer sitting on top of security groups, and T-005 as evidence.

## 06. Logging
`modules/06-logging/` — CTS coverage and T-006, showing a configuration change actually appearing in the log.

## 07. Monitoring
`modules/07-monitoring/` — Cloud Eye thresholds, T-008, and the honest flag that thresholds are still an initial estimate (RR-01).

## 08. Security Test
`validation/test-register.md` — walk through the full table, not just one test, to show the coverage as a set rather than a single example.

## 09. Backup Restore
`modules/08-backup-recovery/restore-test.md` — the actual restore test record, including what it does and doesn't prove.

## 10. Final Posture
`docs/design-baseline-score.md` and `validation/findings-summary.md` — close on the score and the dashboard, including the two open items (monitoring tuning, incident response tabletop) stated plainly rather than glossed over.

## Notes for whoever is presenting this

The strongest moment in this walkthrough is usually step 10, specifically the fact that the score isn't 100/100 and the reasoning for why not is right there in the document. A reviewer tends to trust a project more, not less, once they see the honest gaps stated next to the parts that are fully validated.
