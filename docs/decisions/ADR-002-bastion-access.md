# ADR-002: Use a Bastion Host Instead of Direct SSH to Application Servers

## Decision
All administrative SSH access goes through a single bastion host in the public subnet. Application servers in the private subnet have no direct SSH exposure to the internet.

## Why
A bastion host consolidates the administrative attack surface into one hardened, monitored point instead of spreading it across every instance that needs occasional administrative access.

## Alternatives Considered
- **Direct SSH to each application server with a public IP:** removed early, since it would mean N attack surfaces instead of one, each needing to be independently hardened and monitored.
- **VPN-only access with no bastion:** a reasonable alternative and arguably stronger, but adds infrastructure and cost beyond the scope of this project. Noted as a possible future enhancement rather than implemented here.

## Security Impact
Concentrates administrative risk onto a single, well-monitored host rather than distributing it. The tradeoff is that the bastion becomes a high-value target, which is why it carries the tightest security group rule (source-IP-restricted SSH only) in the entire environment.
