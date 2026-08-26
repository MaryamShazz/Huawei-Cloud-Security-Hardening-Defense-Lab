# Residual Risk Register

`risk/risk-assessment.md` rates risk before and after mitigation. This register tracks specifically the risks that remain at Medium (or higher) residual severity after every documented control is in place, why they can't be fully closed off yet, and what would close them.

A professional security posture isn't "everything is fully secure." It's being specific about what's left, why, and what closes the gap. This document exists so those three medium residual items from the risk assessment don't get quietly dropped once the rest of the checklist is complete.

## Register

### RR-01 : Monitoring threshold accuracy

Residual risk: Medium
Why it remains: Cloud Eye thresholds (85% CPU, 90% memory, 85% disk) are set from an initial estimate, not from observed production traffic. A threshold set too high could miss a genuine issue; one set too low produces alert fatigue.
Closes when: Thresholds are retuned after a reasonable observation period against real traffic.
Owner action: Revisit `configs/monitoring/cloud-eye-thresholds-template.json` once production data is available.

### RR-02 : Backup and recovery robustness

Residual risk: Medium
Why it remains: A single successful test restore confirms the process works under one set of conditions. It doesn't confirm the process holds up during an actual incident, under time pressure, or against a corrupted or partial backup.
Closes when: A restore is tested again under simulated incident conditions, ideally as part of the pending tabletop exercise.
Owner action: Schedule a second restore test tied to the incident response tabletop exercise in `docs/incident-response.md`.

### RR-03 : Patch cadence over time

Residual risk: Medium
- Why it remains: A patch schedule is documented as part of the hardening checklist, but a schedule only reduces this risk if it's actually followed consistently over time. A one time hardening pass doesn't guarantee ongoing compliance.
- Closes when: A recurring patch cadence has been followed for at least one full cycle with evidence of compliance.
- Owner action: Track patch application dates against the schedule and revisit this entry after the first full cycle.

## What's explicitly not in this register

Risks that were rated Low residual in `risk/risk-assessment.md` (IAM credential compromise, open security groups, missing audit trail, public storage exposure, lateral movement) aren't repeated here. This register is specifically for what's left over after mitigation, not a restatement of the full risk table.

## Review cadence

This register should be revisited at the same time as `checklists/security-review.md`, since closing an item here usually means a corresponding checklist item also needs reverification.
