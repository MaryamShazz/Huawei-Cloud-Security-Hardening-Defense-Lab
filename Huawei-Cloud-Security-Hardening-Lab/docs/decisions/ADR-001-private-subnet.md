# ADR-001: Split the VPC into Public and Private Subnets

## Decision
The environment uses a single VPC split into a public subnet (bastion only) and a private subnet (ECS workload, no public IP).

## Why
The application workload doesn't need to be directly reachable from the internet — only administrative access and, indirectly, a load balancer or gateway do. Keeping the workload in a private subnet removes an entire class of direct-exposure attacks.

## Alternatives Considered
- **Single flat subnet:** simpler to set up, but any compromised instance would have unrestricted network reach to every other instance. Rejected for the lateral-movement risk it introduces.
- **Public IP on every instance with security groups as the only control:** relies entirely on security group correctness with no network-level backstop. Rejected because a single misconfigured security group would fully expose the instance.

## Security Impact
Removes the internet as a direct attack surface against the workload. Shifts the administrative attack surface entirely onto the bastion host, which is a deliberate tradeoff — one hardened, monitored entry point is easier to defend than many potential entry points.
