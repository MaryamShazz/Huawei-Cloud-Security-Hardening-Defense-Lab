# Permission Matrix — IAM

This is the visible evidence behind the least-privilege review mentioned throughout the repository: what each group can actually do, not just a description of intent.

| Group | IAM | VPC | ECS | OBS | Logging | Admin |
|---|---|---|---|---|---|---|
| Developers | Limited (read own resources) | Read | Limited (start/stop test instances) | App data only | Read | No |
| Operators | Limited (no policy edits) | Manage | Manage | Limited (no bucket policy edits) | Read | No |
| Auditors | Read | Read | Read | Read | Read | No |
| Admins | Full | Full | Full | Full | Full | Yes |

## How to read this

"Limited" means the group can act on specific resources or specific actions within a service, not the service as a whole — for example, Developers can start or stop a test ECS instance but can't modify its security group or terminate a production instance. "Manage" means broader create/update/delete rights within that service, scoped to non-IAM configuration. Only the Admins group has IAM write access, since IAM is the layer every other control depends on and its blast radius if compromised is the largest of any group.

## Why Admins is still a group, not an exception

Even full-access accounts go through the same group-and-MFA structure as everyone else, rather than being configured as one-off "root-equivalent" accounts. That keeps the audit trail (who is an admin, and why) in the same place as every other permission decision.
