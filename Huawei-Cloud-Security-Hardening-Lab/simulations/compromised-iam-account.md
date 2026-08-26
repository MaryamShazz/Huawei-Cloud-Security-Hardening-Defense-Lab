# Simulation —> Compromised IAM Account

*Classification: Planned tabletop exercise (not yet performed).*

This is the scenario documented step-by-step in [`../docs/incident-response.md`](../docs/incident-response.md) (Scenario 01). It has not been walked through with a live account or a real responder yet. It's listed here as a placeholder for that future exercise, not as a completed test.

## What the exercise would involve
A test IAM account would have its credentials deliberately "compromised" (simulated, e.g. by generating a new access key and treating it as leaked) and the response team would work through the documented steps: detect via CTS, disable the account, rotate credentials, review scope, investigate, restore, document.

## Why this hasn't been run yet
Running this properly needs a dedicated block of time with the people who'd actually respond, plus a safe way to simulate the compromise without creating real risk. Both are being scheduled rather than skipped. Tracked in `risk/residual-risk-register.md` (RR-02, adjacent) and `validation/test-register.md` (T-010).

## Status
NOT TESTED -> documented design only.
