# 🖥️ Backend

> **Status:** Not implemented by design.

This folder intentionally contains no backend code.

---

## Why There Is No Backend

A production backend for this dashboard would need to authenticate with a real Huawei Cloud account and query services such as **IAM, VPC, Cloud Eye,** and **Cloud Trace Service (CTS)** to retrieve live security and configuration data.

Implementing a backend that simply returned hardcoded JSON would give the impression that the dashboard was performing real time validation when it was not.

Instead, the project deliberately uses a static frontend that presents a documented design snapshot. This approach accurately reflects the current state of the project without overstating its capabilities.

---

## What a Production Backend Would Require

A complete implementation would include:

- Read-only Huawei Cloud credentials for services such as IAM, VPC, Security Groups, Cloud Firewall, OBS, CTS, and Cloud Eye.
- A lightweight API service (for example, using Node.js or Python) to query Huawei Cloud APIs and map the results to the PASS, FAIL, and PARTIAL checks documented in `validation/test-register.md`.
- A scheduled refresh process to periodically update dashboard data rather than querying cloud services on every page load.
- Secure credential management, with secrets stored outside the repository in accordance with `SECURITY.md`.

---

## Current Status

The backend is intentionally not implemented.

Its design is discussed as a potential future enhancement in `docs/design-baseline-score.md`. Because the dashboard does not claim to display live cloud data, the absence of a backend is considered a design decision rather than a project limitation.