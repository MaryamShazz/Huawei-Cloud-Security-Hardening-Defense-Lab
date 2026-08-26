# ☁️ Cloud Hardening Checklist

> Mark each item as the environment is implemented and verified. A checkmark should only be added when the corresponding control has been configured and, where applicable, validated with evidence.

📖 Supporting rationale for each control is available in [`docs/hardening-guide.md`](../docs/hardening-guide.md).

---

## 🔐 Identity & Access

- [ ] Permissions assigned through groups, not individual accounts
- [ ] MFA enforced on all accounts with console access
- [ ] Password policy configured (minimum length, rotation, and lockout threshold)
- [ ] Permission matrix reviewed against actual job functions for each group
- [ ] No account holds administrator access unless the role genuinely requires it

---

## 🌐 Network

- [ ] VPC and subnet CIDR ranges documented
- [ ] Public and private subnets clearly separated
- [ ] Internet Gateway route present only in the public subnet route table
- [ ] Private subnet route table confirmed to have no direct internet path
- [ ] NAT configured for outbound access from the private subnet only

---

## 🛡️ Security Groups

- [ ] Bastion security group restricts SSH access to approved source IP addresses
- [ ] Application tier security group accepts traffic only from the bastion host and required ports
- [ ] Database tier security group accepts traffic only from the application tier
- [ ] No security group allows inbound administrative access from `0.0.0.0/0`
- [ ] Outbound rules reviewed rather than left at the default allow-all configuration

---

## 🚧 Cloud Firewall

- [ ] Allow list matches documented expected traffic
- [ ] Deny list covers known malicious ranges
- [ ] Rules tested against both legitimate and blocked traffic

---

## 🪣 Object Storage

- [ ] All buckets private by default
- [ ] Server-side encryption enabled
- [ ] Versioning enabled
- [ ] Any public access documented with a specific justification
- [ ] Signed URLs used for external sharing instead of public buckets

---

## 📋 Logging

- [ ] Cloud Trace Service enabled account-wide
- [ ] Administrative actions confirmed to appear in logs
- [ ] Logs routed to a location that audited accounts cannot modify

---

## 📈 Monitoring

- [ ] Cloud Eye enabled on all ECS instances
- [ ] Alert thresholds configured based on the expected baseline
- [ ] Alerts confirmed to reach the configured notification channel

---

## 💾 Backup

- [ ] Snapshot schedule configured
- [ ] Restore process documented
- [ ] At least one test restore successfully performed

---

## 🔒 General Hardening

- [ ] Unused services and ports disabled
- [ ] Instances reviewed for current security patches
- [ ] Secrets, credentials, private keys, and access tokens excluded from the repository
- [ ] Checklist repeated after any major configuration change