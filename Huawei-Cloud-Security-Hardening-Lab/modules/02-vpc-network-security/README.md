# 02 — VPC Network Security

## Objective
Segment the network so a compromise on one side doesn't automatically reach the other.

## Why It Matters
A flat network means a single compromised host can reach anything else in the VPC. Splitting public and private subnets forces an attacker through more checkpoints.

## Configuration
- VPC with defined CIDR range
- Public subnet: bastion host only
- Private subnet: ECS instances, no public IP
- Internet Gateway attached only to the public subnet's route table
- NAT configured for private subnet outbound-only access

Full detail: [`docs/architecture.md`](../../docs/architecture.md), [`docs/deployment-guide.md`](../../docs/deployment-guide.md).

## Screenshots
See [`screenshots/vpc/`](../../screenshots/vpc/).

## Security Benefit
Removes any direct path from the public internet to the actual application workload.

## Best Practices
Route tables should be checked directly, not assumed correct — an unintended route to the Internet Gateway is a common and easy-to-miss setup mistake.

## Security Engineer's Notes
Segmentation alone doesn't stop a breach. It buys time and forces more checkpoints, which is what gives logging and monitoring a chance to catch what's happening.

## Further Detail
Step-by-step implementation notes: [`implementation.md`](implementation.md), subnet plan: [`subnet-plan.md`](subnet-plan.md), route review: [`route-review.md`](route-review.md). Screenshots: [`screenshots/`](screenshots/).
