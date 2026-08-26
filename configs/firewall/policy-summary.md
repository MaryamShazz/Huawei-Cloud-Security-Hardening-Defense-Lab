# ☁️ Cloud Firewall Policy Summary

This document provides a human readable summary of [`firewall-rules-template.json`](./firewall-rules-template.json).

| Rule | Type | Protocol / Port | Source → Destination | Purpose |
|------|------|-----------------|----------------------|---------|
| `allow-https-inbound` | Allow | TCP 443 | `0.0.0.0/0` → Public entry point | Allows public HTTPS access. Traffic should never connect directly to private instances. |
| `allow-admin-vpn` | Allow | TCP 22 | Admin CIDR → Bastion | Allows administrative access and mirrors the bastion security group. |
| `deny-known-bad-range` | Deny | Any | Blocklisted CIDR → Any | Blocks traffic originating from known malicious address ranges identified through threat intelligence. |

> Note: This summary is provided for readability. The JSON template remains the authoritative source for the firewall policy configuration.