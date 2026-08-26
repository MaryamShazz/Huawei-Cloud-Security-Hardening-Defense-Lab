# Restore Test Record

**Status: Procedure designed and documented. Not yet executed — no live Huawei Cloud environment has been deployed, so no snapshot has actually been taken or restored.**

**Test type (once executable):** Controlled test restore (not an incident-driven restore)
**Source:** Scheduled snapshot of the ECS application instance
**Target:** A new, isolated test instance (not the original)

## Procedure (as designed)
1. Select the most recent scheduled snapshot.
2. Launch a new instance from that snapshot into an isolated test environment.
3. Verify the instance boots successfully.
4. Spot-check application data on the restored instance against the source instance.

## Expected result
Restore completes successfully, with data on the restored instance matching the source at the time the snapshot was taken.

## What this record does and doesn't currently represent
This is a fully specified test procedure, not a report of a restore that has actually happened. Once a Huawei Cloud account exists and an ECS instance with scheduled snapshots is running, this procedure should be executed for real and this file updated with the actual result, timestamp, and any discrepancy found. Until then, treating this as a completed test would overstate what's actually been done — the gap is tracked in [`risk/residual-risk-register.md`](../../risk/residual-risk-register.md) as RR-02, alongside the deeper point that even a real restore only proves the process works under one clean, planned condition, not under incident pressure.
