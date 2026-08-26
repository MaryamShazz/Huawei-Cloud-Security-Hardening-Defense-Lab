# Subnet Plan

| Subnet | CIDR (example) | Resources | Public IP | Internet Access |
|---|---|---|---|---|
| Public | 10.0.1.0/24 | Bastion host | Yes (bastion only) | Direct, via Internet Gateway |
| Private | 10.0.2.0/24 | ECS instances, application workload | No | Outbound only, via NAT |

CIDR values here are illustrative placeholders — substitute the actual ranges assigned in your account. The plan itself (one subnet with a public entry point, one subnet fully internal) is what matters for the security posture, not the specific numbers.
