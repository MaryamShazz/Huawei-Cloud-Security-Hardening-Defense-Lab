# Hardening Guide

This is the reasoning behind the hardening checklist, not just the checklist itself. Each control below maps to an item in `checklists/cloud-hardening.md`.

## Identity

Least privilege only works if it's actually enforced, not just written down somewhere. Every group's permissions should be reviewed against what its members actually do, and anything broader than that gets trimmed. MFA matters most on accounts with any administrative capability; a compromised password without MFA on an admin account is close to a full account takeover.

## Network

Every subnet should have a specific job. If a resource doesn't need a public IP, it shouldn't have one. Route tables should be checked directly rather than assumed correct; it's easy to leave a route to an Internet Gateway attached to the wrong subnet during setup and not notice until something is exposed that shouldn't be.

## Security Groups

Default-deny is the right starting point for every security group; rules get added for what's actually needed, not removed from something permissive. Port 22 and remote desktop ports are the two most commonly left open to the whole internet, and they're also the two most targeted by automated scanning.

> **Common Misconfiguration**
> A database security group that allows inbound traffic from `0.0.0.0/0` on its database port is one of the most common findings in cloud security reviews. It should only ever accept traffic from the specific application tier that needs it.

## Storage

Public buckets are usually public by accident, not by decision. Setting private-by-default and requiring an explicit, documented reason to make anything public catches most of these before they become a problem. Encryption at rest and versioning are both cheap to enable and expensive to have skipped after data loss or a breach.

## Logging and Monitoring

Logging without monitoring just produces a record after the fact. Monitoring without logging means an alert fires but there's no way to trace what actually happened. Both need to be in place together, and both need someone actually watching the alerts, not just collecting them.

## Patching

Unpatched services are one of the more common paths to compromise, and one of the more preventable. A patch schedule, even a simple one, closes off a large share of opportunistic attacks that rely on known, already-fixed vulnerabilities.

## General principle

Every control above trades some convenience for security. That trade-off is deliberate, and it's worth being able to explain why each one is there rather than treating the checklist as a box-ticking exercise.
