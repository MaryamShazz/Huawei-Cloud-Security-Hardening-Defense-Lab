# Simulation —> Storage Access Incident

*Classification: Designed simulation — not yet executed against live infrastructure.*

This corresponds to T-007 in [`../validation/test-register.md`](../validation/test-register.md), described here as an incident style walkthrough rather than a single pass/fail test.

## Setup (as designed)
- An unauthenticated request would be made against a bucket object URL, no signed URL or credentials attached.

## Expected outcome
Access denied.

## Actual outcome
Not yet observed —> pending deployment of a live Huawei Cloud environment and creation of a real OBS bucket.

## What a real incident investigation would add beyond this test
This test only checks the "front door." A real storage access incident investigation would also need to check CTS for unusual access patterns on the bucket over time, which requires real traffic history that won't exist until the environment has been live for a while.
