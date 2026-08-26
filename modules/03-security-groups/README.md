# 03 — Security Groups

## Objective
Enforce instance-level, stateful traffic filtering scoped to what each tier actually needs.

## Why It Matters
Security groups are the last line of defense at the instance level. Left permissive, they undo the benefit of network segmentation entirely.

## Configuration
- Default-deny starting point for every group
- Bastion: SSH restricted to known administrative source IPs
- Application tier: inbound limited to bastion + load balancer tier
- Database tier: inbound limited to the application tier's security group only

See [`configs/security-groups/`](../../configs/security-groups/) for the rule templates.

## Screenshots
See [`screenshots/security-groups/`](../../screenshots/security-groups/).

## Security Benefit
Restricts lateral movement — even a compromised bastion still has to get past a second set of rules to reach the application or database tier.

## Best Practices
Never leave an administrative port (SSH, RDP) or a database port open to `0.0.0.0/0`. Test connectivity after configuring, rather than assuming rules behave as written.

## Security Engineer's Notes
The database tier row in the config template is the one most worth double-checking by hand — it's the single most common finding in real cloud security reviews.

## Further Detail
Step-by-step implementation notes: [`implementation.md`](implementation.md), rule matrix: [`rule-matrix.md`](rule-matrix.md). Screenshots: [`screenshots/`](screenshots/).
