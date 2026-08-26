# Implementation Detail — Cloud Firewall

1. Enable Cloud Firewall on the VPC.
2. Add an allow-list rule for HTTPS (443) inbound to the public-facing entry point.
3. Add an allow-list rule for administrative SSH (22) scoped to the admin IP range, mirroring the bastion security group as a second layer.
4. Add deny-list entries for any known-bad ranges relevant to the deployment (threat intelligence feed, prior abuse sources, etc).
5. Send test traffic matching both an allowed and a denied pattern, and confirm the firewall behaves as configured before considering it live.

Reference: [`configs/firewall/policy-summary.md`](../../configs/firewall/policy-summary.md) and [`configs/firewall/firewall-rules-template.json`](../../configs/firewall/firewall-rules-template.json).
