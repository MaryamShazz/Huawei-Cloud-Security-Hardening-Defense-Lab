# Simulation —> Suspicious Configuration Change

**lassification: Designed simulation — not yet executed against live infrastructure.* This describes a planned test, not something that has been run against a real account.

This corresponds to T-006 in [`../validation/test-register.md`](../validation/test-register.md), described here from the "suspicious change detection" angle rather than the "logging coverage" angle.

## Setup (as designed)
- A test security group rule would be added and then removed by an account with legitimate access, as a stand in for what an unauthorized change would look like in the logs.

## Expected outcome
The change appears in the CTS log with the correct actor, action, and timestamp, and would be visually distinguishable from a planned deployment change if reviewed without prior context.

## Actual outcome
Not yet observed —> pending deployment of a live Huawei Cloud environment and enablement of Cloud Trace Service.

## What this would and wouldn't demonstrate, once run
Running this would confirm the logging pipeline works. It wouldn't confirm a human reviewer would actually notice the change in a timely way without an alert tied to it, that's a process gap, not a logging gap, and wouldn't be addressed by this test alone.
