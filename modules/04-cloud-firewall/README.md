# 04 — Cloud Firewall

## Objective
Add a second, boundary-level filtering layer at the network edge, independent of instance-level security groups.

## Why It Matters
Relying on security groups alone means every filtering decision lives at the instance level. A boundary firewall catches traffic before it ever reaches a subnet.

## Configuration
- Allow list matching documented expected traffic
- Deny list covering known-bad ranges
- Rules tested against both legitimate and blocked sample traffic

See [`configs/firewall/`](../../configs/firewall/) for the rule template.

## Screenshots
See [`screenshots/firewall/`](../../screenshots/firewall/).

## Security Benefit
Reduces the attack surface reaching the VPC at all, rather than depending entirely on filtering that happens after traffic is already inside.

## Best Practices
Keep the allow list as narrow as the application actually requires. Review the deny list periodically rather than treating it as a one-time setup.

## Security Engineer's Notes
A firewall rule set is only as good as the traffic patterns it was tested against — untested rules are a guess, not a control.

## Further Detail
Step-by-step implementation notes: [`implementation.md`](implementation.md). Screenshots: [`screenshots/`](screenshots/).
