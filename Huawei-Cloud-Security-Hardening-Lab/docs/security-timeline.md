# Security Timeline

This is the deployment lifecycle in the order it actually happened, restated as a timeline rather than a build checklist. The step-by-step build instructions live in [`docs/deployment-guide.md`](deployment-guide.md); this document is the higher-level story of how the environment moved from provisioned to validated.

```
Environment Provisioned
        │
        ▼
IAM Hardened
        │
        ▼
Network Segmented
        │
        ▼
Firewall Configured
        │
        ▼
Storage Secured
        │
        ▼
Logging Enabled
        │
        ▼
Monitoring Enabled
        │
        ▼
Backup Tested
        │
        ▼
Security Validation
        │
        ▼
Risk Review
```

## What each stage represents

**Environment Provisioned** — a default Huawei Cloud account with no custom configuration: the starting point this entire repository works against.

**IAM Hardened** — groups, MFA, and password policy in place before anything else, since every later stage assumes identity is already trustworthy.

**Network Segmented** — the VPC split into public and private subnets, with the bastion as the only public entry point.

**Firewall Configured** — Cloud Firewall added as a second filtering layer on top of the security groups defined during network segmentation.

**Storage Secured** — buckets set private by default, encrypted, and versioned.

**Logging Enabled** — Cloud Trace Service turned on account-wide, so every stage from this point forward has an audit trail behind it.

**Monitoring Enabled** — Cloud Eye configured with initial alert thresholds, flagged for retuning once real traffic is observed.

**Backup Tested** — snapshots scheduled and a test restore actually performed, not just configured.

**Security Validation** — every control run against its expected result, recorded in [`validation/validation-results.md`](../validation/validation-results.md).

**Risk Review** — the threat model and risk assessment checked against what was actually built, with anything left open logged in [`risk/residual-risk-register.md`](../risk/residual-risk-register.md) rather than dropped.

## Why logging comes before monitoring

Cloud Trace Service was enabled before Cloud Eye deliberately. Once monitoring alerts start firing, having an existing audit trail means any alert can immediately be cross-checked against "was this a planned change" rather than starting the investigation from nothing.

## Why validation comes after every control, not per-control

Validating each control the moment it's configured would miss interactions between controls — for example, a security group rule that looks correct in isolation but conflicts with a Cloud Firewall rule added later. Running validation as its own stage, once every module is in place, is what catches that class of issue.
