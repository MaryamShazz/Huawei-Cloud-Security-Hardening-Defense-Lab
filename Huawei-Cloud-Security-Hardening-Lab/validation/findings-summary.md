# Findings Summary — Design Review Dashboard

*No live Huawei Cloud environment has been deployed yet.* This dashboard previously used PASS/PARTIAL language that implied live testing had occurred. It hasn't. The statuses below reflect design and documentation completeness, not verified live behavior.

```
DESIGN REVIEW

IAM                    DESIGNED
Network Segmentation   DESIGNED
Security Groups        DESIGNED
Cloud Firewall         DESIGNED
Storage Security       DESIGNED
Logging                DESIGNED
Monitoring             DESIGNED (thresholds are an unvalidated initial estimate)
Backup & Recovery      DESIGNED (restore procedure written, not yet executed)
Incident Response      DESIGNED ONLY (tabletop not scheduled)
```

## Open Items

```
01  No live Huawei Cloud account has been provisioned — every item above is pending deployment
02  Monitoring thresholds are an initial estimate with no traffic data behind them yet
03  Backup restore procedure has been written but never executed
04  Incident response tabletop exercise not scheduled
```

## How to read "DESIGNED"

"DESIGNED" means the control has a complete specification: what to configure, how, and how to verify it. It does not mean the control has been configured or verified against a real Huawei Cloud account. Once each control is deployed and its corresponding test in [`test-register.md`](test-register.md) is actually run, this dashboard should be updated per-item to PASS, FAIL, or PARTIAL, and this note removed once every item has real status behind it.

## Local simulation, for reference

[`local-lab/`](../local-lab/README.md) lets you run something resembling several of these tests locally and see real (simulated) output. Its results are not reflected in this table, since a local simulation is not evidence about a live Huawei Cloud account — see the local lab's own README for why that distinction matters.

## Where each open item is tracked

| Open item | Tracked in |
|---|---|
| No live environment yet | This file, `README.md`, `validation/test-register.md` |
| Monitoring threshold tuning | `risk/residual-risk-register.md` |
| Backup/recovery execution | `risk/residual-risk-register.md`, `modules/08-backup-recovery/restore-test.md` |
| Incident response tabletop | `docs/incident-response.md` |

## Overall status

The design and documentation layer is complete across all nine domains. The verification layer, actually running each test against a live account and replacing "Designed" with a real observed result — has not started, and this document says so plainly rather than rounding "designed" up to "passed."
