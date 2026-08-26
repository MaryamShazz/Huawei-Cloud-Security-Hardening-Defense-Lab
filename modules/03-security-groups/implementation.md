# Implementation Detail — Security Groups

1. Create `sg-bastion`, `sg-app-tier`, and `sg-db-tier`.
2. Start every group with no inbound rules (default-deny) and add rules explicitly.
3. `sg-bastion`: allow inbound TCP/22 from the administrative IP range only.
4. `sg-app-tier`: allow inbound TCP/22 from `sg-bastion`, and the application port from the load balancer tier.
5. `sg-db-tier`: allow inbound on the database port from `sg-app-tier` only — nothing else, including the bastion.
6. Test connectivity between tiers to confirm each rule behaves as written, not just as configured.

Reference: `rule-matrix.md` in this folder, and [`configs/security-groups/security-group-templates.json`](../../configs/security-groups/security-group-templates.json).
