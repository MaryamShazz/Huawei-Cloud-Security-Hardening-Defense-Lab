# Incident Response Playbook

**Status: Documented. Tabletop exercise pending.**

This is a working incident response playbook, not a finished, tested runbook. The scenarios below reflect the response process as designed against this environment's logging and monitoring setup. Neither has been walked through as a tabletop exercise yet, and that limitation is stated here deliberately rather than left implicit, because claiming a tested process without actually testing it would misrepresent the state of the project. Tracked alongside `risk/residual-risk-register.md` (RR-02) and `validation/validation-results.md`.

## Scenario 01 — Compromised IAM Account

```
Detect
  │
  ▼
Review CTS logs
  │
  ▼
Identify suspicious actions
  │
  ▼
Disable account
  │
  ▼
Rotate credentials
  │
  ▼
Review permission scope
  │
  ▼
Investigate affected resources
  │
  ▼
Restore secure state
  │
  ▼
Document incident
```

**Detect** — A Cloud Eye alert on abnormal API activity, or a Cloud Trace Service entry that doesn't match any planned change, is the usual trigger.

**Review CTS logs** — Pull the account's recent action history: what was called, from what source, and when.

**Identify suspicious actions** — Flag anything outside the account's normal role, especially IAM changes, security group changes, or firewall rule changes that weren't part of a scheduled deployment.

**Disable account** — Suspend the account immediately rather than investigating first. A live compromised account can keep acting while the investigation is underway.

**Rotate credentials** — Force a credential and MFA reset for the account, and check for any other accounts that might share the same compromised credential.

**Review permission scope** — Confirm exactly what the account could access, since that defines the blast radius of the incident.

**Investigate affected resources** — Check anything the account touched during the suspicious window: security groups modified, buckets accessed, instances started or stopped.

**Restore secure state** — Revert any unauthorized changes found during the investigation (security group rules, IAM policies, firewall rules) back to their known-good state.

**Document incident** — Write up what triggered the detection, what was found, what was done, and whether any control (alert threshold, permission scope, logging coverage) needs adjusting as a result.

**Status: Documented, tabletop exercise pending.**

## Scenario 02 — Compromised ECS Instance

```
Detect (Cloud Eye anomaly or CTS trace)
  │
  ▼
Isolate instance (strip security group rules / move to isolated SG)
  │
  ▼
Snapshot instance before remediation
  │
  ▼
Investigate (logs, running processes, network connections)
  │
  ▼
Rebuild from known-good image or backup
  │
  ▼
Rotate any credentials the instance had access to
  │
  ▼
Document incident
```

**Status: Documented, tabletop exercise pending.**

## Why these two scenarios first

An IAM account compromise and an ECS instance compromise cover the two most direct paths into this environment described in `docs/threat-model.md`: identity-layer compromise and network/runtime-layer compromise. Additional scenarios (storage exposure, DDoS against the public-facing edge) are reasonable next additions but aren't documented yet, so they aren't listed here as if they were.

## What "tested" would actually mean

A tabletop exercise means walking through one of the scenarios above with the people who'd actually respond, using real console access, and timing how long each step takes. That hasn't happened yet. Until it does, this playbook should be read as a documented starting point, not a proven process.
