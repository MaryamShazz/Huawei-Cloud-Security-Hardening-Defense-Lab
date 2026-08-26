# Design Baseline Score

```
DESIGN BASELINE SCORE

87 / 100
```

**This scores the designed architecture, not a verified live environment.** No Huawei Cloud account has been deployed yet, so this number reflects how complete and well-specified each domain's design is, including whether a test procedure and evidence structure exist for it — not whether the control has actually been proven to work. Once real deployment and testing replace these design-stage estimates with observed results, this should be renamed **Validated Security Posture Score** and recalculated from real test outcomes in `validation/test-register.md`.

## Scoring methodology

**Control domains:** 9
**Maximum score:** 100 points, allocated by how central the domain is to the overall threat model in `docs/threat-model.md` (identity and network segmentation carry the most weight since every other control assumes they hold)

| Domain | Max Points | Points Earned | Basis for points earned |
|---|---|---|---|
| IAM | 15 | 15 | Design fully specified (groups, MFA, password policy) and a permission matrix exists (`modules/01-iam/permission-matrix.md`); test procedure defined (T-006-adjacent, EV-IAM-01/02) |
| Network | 15 | 15 | Subnet plan and route table review fully specified (`modules/02-vpc-network-security/`); test procedure defined (EV-VPC-01) |
| Security Groups | 15 | 15 | Full tiered rule matrix specified (`modules/03-security-groups/rule-matrix.md`); test procedures defined (T-001, T-004) |
| Firewall | 10 | 10 | Allow/deny policy fully specified; test procedure defined (T-005) |
| Storage | 10 | 10 | Bucket security settings fully specified; test procedure defined (T-007) |
| Logging | 10 | 10 | CTS coverage fully specified; test procedure defined (T-006) |
| Monitoring | 10 | 7 | Alert configuration specified, but thresholds are an initial estimate with no supporting traffic data (RR-01) — three points deducted for that gap |
| Backup | 5 | 5 | Restore procedure fully specified and written step by step (`modules/08-backup-recovery/restore-test.md`), even though it hasn't been executed yet — full design points awarded since the procedure itself is complete |
| Incident Response | 10 | 0 | Two scenarios documented, but no tabletop exercise scheduled and no execution timeline set — zero points rather than partial credit, since an unscheduled exercise carries no more assurance than an undocumented one at the design-completeness level this score measures |
| **Total** | **100** | **87** | |

## Why Incident Response scores zero, not partial credit

Every other domain's score reflects design completeness — a fully specified procedure earns full points even before live execution, because the score isn't measuring live verification (that's what `test-register.md`'s "Live Execution" column is for). Incident Response scores zero specifically because it lacks something the others have: a committed next step. There are two documented scenarios, but no scheduled date, no assigned participants, and no defined success criteria for the tabletop exercise, which makes it meaningfully less "designed" than, say, the backup restore procedure, which is fully specified down to the verification steps.

## What this score explicitly does not claim

- It is not a compliance certification of any kind.
- It is not evidence that any control has been deployed to Huawei Cloud.
- It is not derived from any test in `validation/test-register.md` actually passing, since none have been executed yet.
- A future version of this document, once real deployment happens, will use a different and stricter methodology: points awarded only for tests with a PASS result in `test-register.md`, not for design completeness.

## The planned evolution of this score

```
   87 / 100                    LIVE DEPLOYMENT                XX / 100
DESIGN BASELINE      ─────────────────────────────►    VALIDATED SECURITY POSTURE
```

Once a real Huawei Cloud account exists and the tests in `validation/test-register.md` are actually executed, this document and its accompanying image (`assets/design-baseline-score.png`) should be retired in favor of a new **Validated Security Posture Score**, calculated only from real PASS/FAIL/PARTIAL results, with its own asset (`assets/validated-security-posture.png`). The two scores should never be conflated — a design score measures how complete the plan is; a validated score measures how the live environment actually behaved.

## What would move the score right now (before any deployment)

- Scheduling the incident response tabletop exercise with a date and participants: Incident Response to at least partial credit.
- Nothing else changes the design score further, since every other domain is already fully specified. The next real increase in rigor comes from deployment and testing, not from more documentation.
