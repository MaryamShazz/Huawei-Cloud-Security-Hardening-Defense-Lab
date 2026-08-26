# Validation Results

*No live Huawei Cloud environment has been deployed yet.* Every entry below describes a designed test procedure, what would be checked, how, and what result would confirm the control — rather than a result actually observed against a real account. This document previously stated some of these as completed ("PASS," "Restore completed successfully," "Change captured as expected"); that language has been corrected here to avoid implying testing that hasn't happened. See [`local-lab/`](../local-lab/README.md) for a runnable local simulation that exercises the same logic and produces genuine (but clearly labeled as simulated) output.

Each entry follows the same format: the control being tested, what should happen, how it would be tested, and its current status.

## IAM

**Control:** MFA required for console login
**Expected:** Console login blocked without a valid MFA code
**Test procedure:** Attempt console login with correct password, no MFA code entered
**Status:** Designed — pending live execution in Huawei Cloud

**Control:** Group-based least privilege
**Expected:** Accounts in the operators group cannot perform IAM actions (create/delete users, policies)
**Test procedure:** Attempt an IAM write action from an operators-group test account
**Status:** Designed — pending live execution in Huawei Cloud

## Network

**Control:** Private subnet has no direct route to the internet
**Expected:** No route table entry pointing the private subnet to the Internet Gateway
**Test procedure:** Route table inspection for the private subnet
**Status:** Designed — pending live execution in Huawei Cloud (the architecture has been reviewed on paper against this requirement; the live route table has not yet been inspected because no VPC has been provisioned)

## Security Groups

**Control:** SSH restricted to administrative IP range
**Expected:** Internet-wide SSH access denied
**Test procedure:** Connection attempt to the bastion's SSH port from a source IP outside the allowed range
**Status:** Designed — pending live execution in Huawei Cloud

**Control:** Database tier only reachable from application tier
**Expected:** Direct connection attempt from the bastion or the internet to the database port is refused
**Test procedure:** Connection attempt to the database port from the bastion host
**Status:** Designed — pending live execution in Huawei Cloud

## Cloud Firewall

**Control:** Deny list blocks known-bad ranges
**Expected:** Traffic from a blocklisted test range is dropped at the firewall before reaching a subnet
**Test procedure:** Simulated traffic from a range placed on the deny list
**Status:** Designed — pending live execution in Huawei Cloud

## Object Storage

**Control:** Buckets are private by default
**Expected:** Anonymous access to a bucket object is denied
**Test procedure:** Unauthenticated request to a bucket object URL
**Status:** Designed — pending live execution in Huawei Cloud

## Logging

**Control:** Administrative actions are captured by Cloud Trace Service
**Expected:** A test IAM or security group change appears in the CTS log with actor, action, and timestamp
**Test procedure:** Perform a test security group rule change and review CTS output
**Status:** Designed — pending live execution in Huawei Cloud

## Monitoring

**Control:** Cloud Eye alert fires when a threshold is crossed
**Expected:** An alert triggers once CPU utilization crosses the configured threshold for the configured evaluation period
**Test procedure:** Apply synthetic load to a test instance to cross the CPU threshold
**Status:** Designed — pending live execution in Huawei Cloud. Thresholds are also flagged in `risk/residual-risk-register.md` (RR-01) as needing retuning once real traffic is available, independent of whether the test itself has been run.

## Backup and Recovery

**Control:** Snapshot restore produces a working instance
**Expected:** A restored snapshot boots successfully with data intact
**Test procedure:** Restore a snapshot to a new test instance and verify data integrity
**Status:** Designed — pending live execution in Huawei Cloud. A restore procedure has been written out step by step in `modules/08-backup-recovery/restore-test.md`, but no snapshot has actually been taken or restored yet, since no ECS instance has been provisioned.

## Incident Response

**Control:** Documented incident response scenario for a compromised IAM account
**Expected:** Response steps are clear enough to follow without improvisation during an actual incident
**Test procedure:** Tabletop exercise walking through the scenario
**Status:** Designed only — tabletop exercise not scheduled. See `docs/incident-response.md`.

## Summary

Every control in this document has a fully specified test procedure. None have been executed against a live Huawei Cloud account, because no live account has been provisioned yet. This is stated directly here, in `validation/test-register.md`, and in the README, rather than left ambiguous. Once a Huawei Cloud environment exists, each status above should be updated in place to the real observed result (PASS, FAIL, or PARTIAL), with a corresponding evidence record filled in under `evidence/`.
