# Evidence Index

This indexes the [`evidence/`](../evidence/) directory, which organizes proof of each control by domain rather than by module. Where `modules/*/screenshots/` holds raw console captures, `evidence/` holds structured records: which control, which test, what was expected, what was actually observed, and where the supporting screenshot or log lives.

## Structure

```
evidence/
├── IAM/
├── VPC/
├── Security-Groups/
├── Firewall/
├── OBS/
├── CTS/
├── Cloud-Eye/
├── Backup/
└── Validation/
```

Each domain folder contains one evidence record per control, using the format:

```
Evidence ID
Control
Test
Expected Result
Observed Result
Screenshot / Log
Status
```

## Current status

Every domain folder currently contains a template record with the ID, control, and expected result filled in and the observed result and screenshot/log fields left for the actual account evidence once it's captured. This keeps the structure ready to fill in rather than fabricating console output that doesn't exist yet.

## Index

| Domain | Evidence Records |
|---|---|
| [`IAM/`](../evidence/IAM/) | EV-IAM-01 (MFA enforcement), EV-IAM-02 (group-scoped permissions) |
| [`VPC/`](../evidence/VPC/) | EV-VPC-01 (private subnet route table) |
| [`Security-Groups/`](../evidence/Security-Groups/) | EV-SG-01 (tiered rule enforcement) |
| [`Firewall/`](../evidence/Firewall/) | EV-FW-01 (edge allow/deny enforcement) |
| [`OBS/`](../evidence/OBS/) | EV-OBS-01 (private bucket access denial) |
| [`CTS/`](../evidence/CTS/) | EV-CTS-01 (administrative action logging) |
| [`Cloud-Eye/`](../evidence/Cloud-Eye/) | EV-CE-01 (threshold alert delivery) |
| [`Backup/`](../evidence/Backup/) | EV-BK-01 (restore test) |
| [`Validation/`](../evidence/Validation/) | EV-VAL-01 (full test register cross-check) |

Each entry corresponds to a row in [`test-register.md`](test-register.md) or [`control-matrix.md`](control-matrix.md).
