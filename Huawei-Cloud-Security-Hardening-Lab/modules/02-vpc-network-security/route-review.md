# Route Table Review

| Route Table | Destination | Target | Purpose |
|---|---|---|---|
| Public subnet RT | 0.0.0.0/0 | Internet Gateway | Allows the bastion direct internet reachability |
| Public subnet RT | 10.0.0.0/16 (VPC CIDR) | local | Internal VPC traffic |
| Private subnet RT | 0.0.0.0/0 | NAT Gateway | Outbound-only internet access for updates |
| Private subnet RT | 10.0.0.0/16 (VPC CIDR) | local | Internal VPC traffic |

The line that actually matters for this architecture is the absence of a private-subnet route pointing to the Internet Gateway. That single missing route is what keeps the private subnet from being directly reachable from the internet, regardless of what security groups say. This table should be checked against the live route table directly, not assumed to match this plan.
