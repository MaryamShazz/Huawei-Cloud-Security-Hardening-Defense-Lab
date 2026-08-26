# ADR-005: Account-Wide Cloud Trace Service Logging

## Decision
Cloud Trace Service is enabled account-wide, capturing IAM, VPC, security group, firewall, storage, and compute actions, with logs routed to a destination the audited accounts can't edit or delete.

## Why
Partial logging (e.g. only logging IAM changes, or only logging from certain services) leaves blind spots that are hard to predict in advance. Account-wide coverage means the question "what happened here" can always be answered, regardless of which service was involved.

## Alternatives Considered
- **Selective logging on high-risk services only:** rejected, since "high-risk" is a judgment call that can be wrong, and the cost of full logging is low relative to the investigative value it provides.
- **Logging to a destination editable by standard accounts:** rejected, since a compromised account could then tamper with or delete the very log that would reveal the compromise.

## Security Impact
Provides the accountability layer that every other control in this environment depends on for post-incident investigation. Without this, containment and recovery in `docs/incident-response.md` would have no reliable source of truth to work from.
