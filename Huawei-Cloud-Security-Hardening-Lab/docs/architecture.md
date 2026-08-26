# 🏗️ Architecture

## 📖 Overview

The proposed environment is built around a single Virtual Private Cloud (VPC) divided into two subnets: one public and one private.

The **public subnet** contains only a bastion host, which serves as the single entry point for administrative access.

The **private subnet** contains the application infrastructure, including ECS instances and their associated storage. These resources are not directly accessible from the public internet and can only be reached through the bastion host over the internal network.

```text
                    Internet
                        │
                 Cloud Firewall
                        │
          ┌─────────────┴─────────────┐
          │                           │
     Public Subnet              Private Subnet
          │                           │
     Bastion Host               ECS Instances
                                      │
                               Object Storage
                                      │
                                Cloud Backup
                                      │
                                  Cloud Eye
                                      │
                              Cloud Trace Service
```

---

# 🧩 Component Breakdown

### 🔥 Cloud Firewall

Cloud Firewall protects the network boundary by filtering inbound and outbound traffic before it reaches the VPC.

It is intended to use an **allow list** for expected traffic while blocking traffic from **known bad** sources through a **deny list**.

---

### 🖥️ Public Subnet

The public subnet contains only the **bastion host**, which is the only resource assigned a public IP address.

Administrative SSH access is intended to pass exclusively through this host, with security group rules restricting access to approved source IP addresses.

---

### 🖥️ Private Subnet

The private subnet is intended to host the application's ECS instances.

These instances would not receive public IP addresses and would only be accessible through the bastion host using the internal network.

> **Note:** No ECS instances have been provisioned as part of this project.

---

### 🗄️ Object Storage

Object Storage Service (OBS) is intended to store application data and backups.

The proposed configuration includes:

- Private buckets
- Encryption at rest
- Object versioning

These controls help reduce the risk of permanent data loss caused by accidental deletion or overwriting.

---

### 💾 Cloud Backup

Cloud Backup is intended to create scheduled snapshots of ECS instances.

These snapshots complement object storage backups by supporting both data recovery and full instance recovery.

---

### 📈 Cloud Eye

Cloud Eye provides monitoring for resources across the environment, including:

- CPU utilization
- Memory usage
- Network activity
- Storage utilization

Alerts can be configured when predefined thresholds are exceeded.

---

### 📝 Cloud Trace Service

Cloud Trace Service records administrative actions and API activity within the cloud environment.

This audit information supports accountability by helping answer questions such as:

> Who made this change, and when was it made?

---

# 🔄 Traffic Flow

1. External traffic first passes through **Cloud Firewall**, where unauthorized traffic is filtered before reaching the VPC.

2. Requests intended for the bastion host are evaluated again by security groups, with SSH access restricted to approved source IP addresses.

3. Administrators connect to resources in the private subnet through the bastion host over the internal network.

4. Communication between ECS instances is controlled by security groups that allow only the ports required by each service.

---

# 🛡️ Security Design Rationale

Separating public and private resources limits unnecessary exposure to the internet.

Instead of placing every system on the same network, administrative access is concentrated through a single hardened bastion host, while application resources remain isolated within the private subnet.

This approach helps reduce opportunities for lateral movement if one system is compromised and provides additional layers of access control before critical resources can be reached.

> ## 💡 Security Insight
>
> Network segmentation does not prevent every breach.
>
> Its primary value is reducing exposure, slowing lateral movement, and creating additional opportunities for monitoring, logging, and access controls to detect suspicious activity before an attacker reaches critical systems.