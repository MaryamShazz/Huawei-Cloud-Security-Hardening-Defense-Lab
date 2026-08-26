# Requirements

## Account

- A Huawei Cloud account with billing enabled (or a free-tier/sandbox account for lab purposes)
- IAM permissions sufficient to create users, groups, policies, VPCs, security groups, ECS instances, OBS buckets, and to enable Cloud Trace Service and Cloud Eye

## Services used

- Identity and Access Management (IAM)
- Virtual Private Cloud (VPC)
- Elastic Cloud Server (ECS)
- Object Storage Service (OBS)
- Cloud Firewall
- Cloud Eye
- Cloud Trace Service (CTS)
- Cloud Backup

## Local tooling (optional, for automation follow-up work)

- Terraform or an equivalent IaC tool, if automating the configuration described in `docs/deployment-guide.md`
- A terminal with SSH access for connecting through the bastion host

## Knowledge prerequisites

- Basic familiarity with cloud networking concepts (subnets, route tables, CIDR notation)
- Basic familiarity with IAM concepts (users, groups, policies, least privilege)
- Completion of, or familiarity with, the Huawei ICT Academy Cloud Security curriculum is helpful but not required to follow the documentation
