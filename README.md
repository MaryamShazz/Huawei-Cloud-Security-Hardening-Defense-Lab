<div align="center">

# Huawei Cloud Security Hardening & Defense Lab

Timeline: *November 2025 – August 2026*

Designing, securing, and documenting a production ready Huawei Cloud environment through identity management, network isolation, firewall enforcement, monitoring, logging, and infrastructure hardening.

<br>

![Huawei Cloud](https://img.shields.io/badge/Huawei%20Cloud-C7000F?style=for-the-badge)
![Cloud Security](https://img.shields.io/badge/Cloud%20Security-374151?style=for-the-badge)
![IAM](https://img.shields.io/badge/IAM-374151?style=for-the-badge)
![VPC](https://img.shields.io/badge/VPC-374151?style=for-the-badge)
![Security Groups](https://img.shields.io/badge/Security%20Groups-374151?style=for-the-badge)
![Cloud Firewall](https://img.shields.io/badge/Cloud%20Firewall-374151?style=for-the-badge)
![Cloud Eye](https://img.shields.io/badge/Cloud%20Eye-374151?style=for-the-badge)
![Cloud Trace](https://img.shields.io/badge/Cloud%20Trace-374151?style=for-the-badge)
![Threat Model](https://img.shields.io/badge/Threat%20Model-F59E0B?style=for-the-badge)
![Documentation](https://img.shields.io/badge/Documentation-6B7280?style=for-the-badge)
![Portfolio Project](https://img.shields.io/badge/Portfolio%20Project-C7000F?style=for-the-badge)

</div>

---

## Project Mission

This repository documents how a default Huawei Cloud account gets turned into a secure, production-ready environment, following a security engineering methodology rather than a checklist: **Assets → Threats → Controls → Validation**. It covers identity management, network isolation, firewall enforcement, storage protection, monitoring, logging, and infrastructure hardening as one connected security program, backed by a threat model, a control matrix, test-level validation evidence, and a residual risk register that states plainly what's still open.

## Why This Project Exists

Most cloud security coursework ends the moment the lab is marked complete. This repository picks up from there. The Huawei ICT Academy Cloud Security curriculum supplied the starting concepts, the core services and how they work; everything past that point — the architecture decisions, the threat model, the hardening checklist, the risk register, the incident response playbook, the architecture decision records, and the security review — was built independently as a working security portfolio.

The question this project answers isn't "how do I finish the lab." It's closer to: what would a cloud security engineer actually configure, test, and document, if handed a brand-new account and told to secure it before go-live.

> **A note on how to read this repository**
> This repository is the design, documentation, and validation framework for the environment: the architecture, the reasoning, the test scenarios, and the evidence structure. **No live Huawei Cloud environment has been deployed yet.** Earlier drafts of this repository used completed-tense language ("was built," "was confirmed," "a test restore was performed") that overstated this — that language has been corrected throughout to "designed," "documented," and "pending deployment." Screenshots, the Huawei ICT Academy certificate, and any account-specific detail (bucket names, IP ranges, instance IDs) are deliberately left as templates. Anywhere you see "pending real evidence capture," "Designed — pending deployment," or a blank field, that's a spot meant to be completed against your own Huawei Cloud account, not a gap in the documentation itself. [`local-lab/`](local-lab/README.md) is the one part of this repository that's genuinely runnable right now — a local simulation, clearly labeled as such, not a substitute for live Huawei Cloud evidence.

## Architecture

```
                    Internet
                        │
                 Cloud Firewall
                        │
          ┌─────────────┴─────────────┐
          │                           │
     Public Subnet              Private Subnet
          │                           │
     Bastion Host              ECS Instances
                                      │
                               Object Storage
                                      │
                               Cloud Backup
                                      │
                                 Cloud Eye
                                      │
                                 Cloud Trace
```

A full breakdown of each component, the reasoning behind the subnet split, and the traffic flow between layers is in [`docs/architecture.md`](docs/architecture.md). The reasoning behind specific architectural choices (why a bastion, why default-deny, why private storage) is recorded individually in [`docs/decisions/`](docs/decisions/).

## Security Timeline

The deployment lifecycle, from a default provisioned account through to final risk review, is laid out as a timeline in [`docs/security-timeline.md`](docs/security-timeline.md) — a higher-level companion to the step-by-step build order in the deployment guide.

## Security Domains Covered

| Domain | Huawei Cloud Service | What It Protects |
|---|---|---|
| Identity & Access | IAM | Who can act, and what they can act on |
| Networking | VPC, Subnets, Route Tables | Segmentation between public and private resources |
| Perimeter Filtering | Security Groups | Instance-level inbound/outbound traffic |
| Edge Defense | Cloud Firewall | Boundary-level traffic filtering and allow/deny lists |
| Data at Rest | Object Storage Service | Bucket policy, encryption, versioning |
| Visibility | Cloud Eye | CPU, memory, storage, and alert thresholds |
| Accountability | Cloud Trace Service | Administrative and API-level audit logging |
| Continuity | Cloud Backup | Snapshots and disaster recovery |

## Threat Model

Before any control is described, every asset in this environment is mapped to a realistic threat and its attack surface. Full detail: [`docs/threat-model.md`](docs/threat-model.md).

| Asset | Threat | Attack Surface | Existing Control |
|---|---|---|---|
| IAM accounts | Credential compromise | Console / API | MFA + least privilege |
| Bastion host | Brute force | SSH | IP restriction |
| ECS instances | Unauthorized access | Network | Private subnet + security groups |
| Object Storage | Data exposure | Storage API | Private bucket + encryption |
| Cloud configuration | Malicious change | Management APIs | CTS logging |
| Infrastructure | Resource compromise | Runtime | Cloud Eye monitoring |

## Security Control Matrix

Every control maps to a specific security objective and a piece of evidence, not just a config screenshot. Full detail: [`docs/security-controls.md`](docs/security-controls.md), test-level evidence in [`validation/validation-results.md`](validation/validation-results.md).

| Domain | Control | Security Objective | Evidence |
|---|---|---|---|
| IAM | MFA | Account protection | Screenshot + validation IAM-01 |
| IAM | Group-based permissions | Least privilege | Permission matrix |
| VPC | Private subnet | Reduce exposure | Route table |
| Security Groups | Default deny | Restrict lateral movement | Rule set |
| Cloud Firewall | Allow/deny rules | Perimeter filtering | Firewall rules |
| Object Storage | Encryption | Data protection | Bucket config |
| Cloud Trace Service | Audit logging | Accountability | Log evidence |
| Cloud Eye | Alerts | Detection | Monitoring dashboard |
| Cloud Backup | Test restore | Recovery | Restore evidence |

## Skills Demonstrated

Cloud security engineering, threat modeling, identity and access management, network segmentation, firewall configuration, object storage hardening, monitoring and alerting, audit logging, risk assessment, control validation, and technical security documentation.

## Repository Structure

```
Huawei-Cloud-Security-Hardening-Defense-Lab/
├── README.md
├── LICENSE
├── SECURITY.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── requirements.md
├── docs/
│   ├── architecture.md
│   ├── deployment-guide.md
│   ├── threat-model.md
│   ├── security-controls.md
│   ├── hardening-guide.md
│   ├── incident-response.md
│   ├── security-timeline.md
│   ├── design-baseline-score.md
│   ├── demonstration-walkthrough.md
│   ├── execution-roadmap.md
│   ├── theme-style-guide.md
│   └── decisions/
│       ├── ADR-001-private-subnet.md
│       ├── ADR-002-bastion-access.md
│       ├── ADR-003-default-deny-security-groups.md
│       ├── ADR-004-private-object-storage.md
│       └── ADR-005-account-wide-audit-logging.md
├── modules/
│   ├── 01-iam/                        (README, implementation, permission-matrix, screenshots/)
│   ├── 02-vpc-network-security/       (README, implementation, subnet-plan, route-review, screenshots/)
│   ├── 03-security-groups/            (README, implementation, rule-matrix, screenshots/)
│   ├── 04-cloud-firewall/             (README, implementation, screenshots/)
│   ├── 05-object-storage/             (README, implementation, screenshots/)
│   ├── 06-logging/                    (README, implementation, screenshots/)
│   ├── 07-monitoring/                 (README, implementation, screenshots/)
│   ├── 08-backup-recovery/            (README, implementation, restore-test, screenshots/)
│   └── 09-infrastructure-hardening/   (README, hardening-checklist, screenshots/)
├── configs/
│   ├── iam/ ├── network/ ├── security-groups/ ├── firewall/
│   └── storage/ ├── logging/ ├── monitoring/
├── checklists/
│   ├── cloud-hardening.md
│   └── security-review.md
├── risk/
│   ├── threat-model.md (pointer)
│   ├── risk-assessment.md
│   └── residual-risk-register.md
├── validation/
│   ├── test-register.md
│   ├── validation-results.md
│   ├── control-matrix.md
│   ├── findings-summary.md
│   └── evidence-index.md
├── simulations/
│   ├── unauthorized-ssh.md
│   ├── compromised-iam-account.md
│   ├── suspicious-configuration-change.md
│   └── storage-access-incident.md
├── evidence/
│   ├── IAM/ ├── VPC/ ├── Security-Groups/ ├── Firewall/
│   └── OBS/ ├── CTS/ ├── Cloud-Eye/ ├── Backup/ ├── Validation/
├── reports/
│   ├── security-baseline-report.md
│   └── technical-report.pdf
├── dashboard/
│   ├── README.md
│   ├── frontend/index.html
│   └── backend/README.md
├── local-lab/
│   ├── README.md
│   ├── backend/
│   │   └── app.py
│   └── frontend/
│       └── index.html
├── assets/
│   ├── banner.png
│   ├── architecture.png
│   ├── before-after.png
│   ├── attack-surface-before-after.png
│   ├── design-baseline-score.png
│   └── icons/
├── certificates/
│   └── README.md (placeholder — add your own certificate here)
└── references/
    └── references.md
```

## Implementation Modules

Each module below follows the same layout: objective, why it matters, configuration, screenshots, security benefit, best practices, and a closing security engineer's note. Full write-ups live under [`modules/`](modules/); the build order across all of them is in [`docs/deployment-guide.md`](docs/deployment-guide.md).

- **[01 — Identity & Access Management](modules/01-iam/README.md)** — Groups, MFA, password policy, least-privilege review
- **[02 — VPC Network Security](modules/02-vpc-network-security/README.md)** — Public/private subnet split, route tables, NAT
- **[03 — Security Groups](modules/03-security-groups/README.md)** — Tiered, default-deny inbound/outbound rules
- **[04 — Cloud Firewall](modules/04-cloud-firewall/README.md)** — Boundary-level allow/deny lists
- **[05 — Object Storage Security](modules/05-object-storage/README.md)** — Private buckets, encryption, versioning
- **[06 — Logging](modules/06-logging/README.md)** — Account-wide Cloud Trace Service coverage
- **[07 — Monitoring](modules/07-monitoring/README.md)** — Cloud Eye thresholds and alerting
- **[08 — Backup & Recovery](modules/08-backup-recovery/README.md)** — Scheduled snapshots, documented restore procedure
- **[09 — Infrastructure Hardening](modules/09-infrastructure-hardening/README.md)** — Cross-checklist pass across every module above

> **Security Insight**
> IAM is the layer everything else depends on. A firewall rule doesn't matter much if an over-permissioned account can just reconfigure it.

> **Common Misconfiguration**
> Leaving SSH (port 22) or a database port open to `0.0.0.0/0` is one of the fastest ways to attract automated scanning and brute-force traffic.

## Risk Assessment & Residual Risk

The full risk table, rating each threat's impact and likelihood against its mitigation, is in [`risk/risk-assessment.md`](risk/risk-assessment.md). Three risks remain at Medium residual severity even after mitigation — monitoring threshold accuracy, backup/recovery robustness, and patch cadence over time — and are tracked individually, with an owner action and a closing condition, in [`risk/residual-risk-register.md`](risk/residual-risk-register.md). These aren't hidden: a security posture that claims zero remaining risk usually just hasn't looked hard enough.

## Security Validation

**No live Huawei Cloud environment has been deployed yet.** The status below reflects design and documentation completeness, not verified live behavior — see [`validation/findings-summary.md`](validation/findings-summary.md) for the full explanation of what "DESIGNED" means here.

```
DESIGN REVIEW

IAM                    DESIGNED
Network Segmentation   DESIGNED
Security Groups        DESIGNED
Cloud Firewall         DESIGNED
Storage Security       DESIGNED
Logging                DESIGNED
Monitoring             DESIGNED (thresholds unvalidated)
Backup & Recovery      DESIGNED (not yet executed)
Incident Response      DESIGNED ONLY (no tabletop scheduled)
```

```
Open Items
──────────────
01  No live Huawei Cloud account provisioned — everything above is pending deployment
02  Monitoring thresholds are an estimate with no real traffic data behind them
03  Incident response tabletop exercise not scheduled
```

Full dashboard: [`validation/findings-summary.md`](validation/findings-summary.md). Test-by-test detail for every control (expected result, test procedure, current status) is in [`validation/validation-results.md`](validation/validation-results.md).

## Design Baseline Score

The scores the completeness of the *design*, not a verified live posture — it will be renamed **Validated Security Posture Score** and recalculated from real test results once actual deployment happens. Full scoring methodology, including exactly why each domain earned the points it did, is in [`docs/design-baseline-score.md`](docs/design-baseline-score.md).

## Security Test Register

Every test designed for this environment is indexed in one table in [`validation/test-register.md`](validation/test-register.md), from T-001 (unauthorized SSH) through T-010 (incident response tabletop). Each is marked "Designed" with "Live Execution: Pending deployment" — none have been run against a real Huawei Cloud account yet.

## Evidence Pack

Structured, per-control evidence templates (not just raw screenshots) live under [`evidence/`](evidence/), organized by domain (`IAM/`, `VPC/`, `Security-Groups/`, `Firewall/`, `OBS/`, `CTS/`, `Cloud-Eye/`, `Backup/`, `Validation/`). Each template follows the same format: evidence ID, control, test, expected result, an observed-result field marked "pending real evidence capture," a screenshot/log slot, and status. Index: [`validation/evidence-index.md`](validation/evidence-index.md).

## Security Test Scenarios & Simulations

Beyond the individual tests in the register, [`simulations/`](simulations/) documents four scenario-level walkthroughs — unauthorized SSH, a compromised IAM account, a suspicious configuration change, and a storage access incident — each labeled honestly as a **designed simulation not yet executed against live infrastructure** or a **planned tabletop exercise not yet performed**. Nothing here is described as having actually happened against a real account, because it hasn't yet.

## Local Lab (Runnable Simulation)

[`local-lab/`](local-lab/README.md) is a small, genuinely runnable local application — start it with `python backend/app.py` and open `http://localhost:5000` — that implements a **rule-based local security validation simulator based on this project's designed Huawei Cloud architecture** (not a Huawei Cloud emulator, and not a reproduction of any real Huawei API). It lets you actually execute tests resembling T-001 through T-009 against that local model, plus four generalized rule testers (Network, Firewall, Security Group, Monitoring) that take arbitrary input. Every result it produces is real in the sense that real code actually ran and evaluated the rule; the UI labels every result **LOCAL SIMULATION** throughout, because it is not live Huawei Cloud telemetry and is never presented as such. See [`docs/execution-roadmap.md`](docs/execution-roadmap.md) for how this fits into the bigger picture and what comes after it.

## Execution Roadmap

This project is really three layers — the cloud architecture, the security engineering case study wrapped around it, and the runnable local lab — and [`docs/execution-roadmap.md`](docs/execution-roadmap.md) lays out exactly what's complete, what a live Huawei Cloud deployment would add, and the five concrete stages between here and a fully validated environment (local verification → improve the local lab → deploy to Huawei Cloud → connect real evidence → optional live dashboard integration). Nothing in the repository structure needs to change to get there — just placeholders getting replaced with real results, one test at a time.

## Security Validation Console (Dashboard)

A small static dashboard in [`dashboard/`](dashboard/) presents the findings summary and posture score visually. It's an evidence-driven snapshot view of documents already in this repository, not a live connection to a real Huawei Cloud account — see [`dashboard/README.md`](dashboard/README.md) for exactly what it is and isn't. Open [`dashboard/frontend/index.html`](dashboard/frontend/index.html) directly in a browser to view it.

## Incident Response

A documented playbook for two scenarios — a compromised IAM account and a compromised ECS instance — walks through detection, containment, and recovery using this environment's actual logging and monitoring setup. **Status: documented, tabletop exercise not yet performed.** That limitation is stated directly in [`docs/incident-response.md`](docs/incident-response.md) rather than glossed over.

## Architecture Decision Records

Five ADRs record the reasoning behind the core design choices, including the alternatives considered and why they weren't used: [`docs/decisions/`](docs/decisions/). These are the answers to questions like *why a bastion instead of direct SSH to application servers* or *why default-deny instead of default-allow with cleanup later*.

## Security Best-Practice Mapping

Every control is grounded in a recognized general practice, referenced (not certified) in [`references/references.md`](references/references.md). This repository does not claim formal compliance or certification against CIS or any other standard.

## Screenshots

Console screenshots for each module go in [`screenshots/`](screenshots/), organized by domain (`iam/`, `vpc/`, `security-groups/`, `firewall/`, `storage/`, `logging/`, `monitoring/`, `backup/`) as the environment is built out. Each one is meant to sit next to a short note on what it shows and why it matters.

## Project Demonstration

A suggested walkthrough order for presenting this project — architecture through final posture score — is in [`docs/demonstration-walkthrough.md`](docs/demonstration-walkthrough.md).

## Learning Outcomes

Building this made the gap between "configuring a service" and "securing an environment" a lot more concrete. Writing an actual threat model before the controls, instead of after, changed the order decisions got made in — a control now had to answer to a specific threat rather than just being "good practice" in the abstract. The validation and residual risk layers mattered more than expected too: it's one thing to say a control is in place, and a different thing to have a test result and an honestly-labeled gap behind that claim.

## Future Enhancements

- Automate the security group, firewall, and IAM configuration with Terraform or Huawei Cloud's own IaC tooling — not yet implemented, tracked here as a roadmap item only
- Tune monitoring thresholds once real production traffic is available
- Run the pending incident response tabletop exercise and a second backup restore test under simulated conditions
- Add a CloudEye-to-alerting pipeline (email or webhook) for real-time notification
- Add cost-awareness notes alongside the security controls, since hardening decisions aren't free

## References

Full list in [`references/references.md`](references/references.md): Huawei Cloud IAM, VPC, Security Group, Cloud Firewall, CTS, Cloud Eye, and Cloud Backup documentation, plus CIS Cloud Security Benchmarks as a general reference.

## Huawei ICT Academy Foundation

**From Training to Implementation**

This repository builds on the Huawei ICT Academy Cloud Security curriculum. The Academy labs introduced the core services and concepts; this project reorganizes and extends them into a structured implementation guide that reflects how a cloud security engineer would actually approach securing an environment — threat model first, controls mapped to objectives, evidence behind every claim, and open risks tracked rather than hidden. Every section here documents not just what was configured, but why it improves the security of a production cloud environment.

The certificate itself belongs in [`certificates/`](certificates/) once available.

---

<div align="center">
<sub>Portfolio project · Huawei Cloud Security</sub>
</div>
