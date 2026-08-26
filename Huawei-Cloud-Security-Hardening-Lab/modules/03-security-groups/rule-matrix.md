# Network Rule Matrix

| Source | Destination | Port | Purpose | Decision |
|---|---|---|---|---|
| Admin IP range | Bastion | 22 | Administration | Allow |
| Internet | ECS (app tier) | 22 | Direct SSH | Deny |
| Bastion | ECS (app tier) | 22 | Administration | Allow |
| Load balancer tier | ECS (app tier) | 8080 | Application traffic | Allow |
| Application tier | Database tier | DB port | Application traffic | Allow |
| Internet | Database tier | DB port | Public access | Deny |
| Bastion | Database tier | DB port | Direct admin access to DB | Deny |

This table is a more direct way to read the security posture than a stack of console screenshots — every row is a decision, and every "Deny" row exists to close a specific path an attacker would otherwise have. The "Bastion → Database: Deny" row is deliberate: administrators reach the database through the application tier's own access patterns, not directly, keeping the bastion's blast radius limited to what it's actually meant for.
