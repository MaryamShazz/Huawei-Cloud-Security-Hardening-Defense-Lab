# Simulation —> Unauthorized SSH Attempt

*Classification: Designed simulation — not yet executed against live infrastructure.* No Huawei Cloud account has been provisioned yet, so this test has not actually been run against a real bastion host. A runnable local approximation of this exact test exists in [`../local-lab/`](../local-lab/README.md), clearly labeled as a local simulation rather than live Huawei Cloud telemetry.

This corresponds to T-001 in [`../validation/test-register.md`](../validation/test-register.md).

## Setup (as designed)
- Source: a test IP address deliberately outside the admin CIDR range configured in `configs/security-groups/security-group-templates.json`
- Target: bastion host, port 22

## Expected outcome
Connection refused at the security group layer before reaching the SSH daemon.

## Actual outcome
Not yet observed —> pending deployment of a live Huawei Cloud environment.

## What this would and wouldn't demonstrate, once run
Running this for real would confirm the specific rule works against one test source. It wouldn't demonstrate resistance to a distributed or spoofed source attack, which needs a different test design entirely.
