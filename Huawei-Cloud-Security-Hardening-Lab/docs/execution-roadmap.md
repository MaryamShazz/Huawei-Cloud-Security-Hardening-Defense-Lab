# Execution Roadmap

This document exists to answer one question directly: **what happens after this repository, and in what order.** It also names the three distinct layers this project is actually made of, since it's easy to lose track of that once there are 100+ files.

## The three layers inside this project

**1. The Cloud Security Architecture** — the formal Huawei Cloud design: IAM → VPC → Security Groups → Cloud Firewall → OBS → CTS → Cloud Eye → Backup, with public/private subnet separation and bastion-based administrative access. This is `docs/architecture.md`, `modules/`, and `configs/`.

**2. The Security Engineering Case Study** — the professional layer wrapped around that architecture: Threat Model → Security Control Matrix → Risk Assessment → Residual Risk → ADRs → Best-Practice Mapping → Incident Response → Security Validation. This is `docs/threat-model.md`, `docs/security-controls.md`, `risk/`, `docs/decisions/`, `references/`, and `validation/`. This layer is what separates the project from a course lab writeup.

**3. The Runnable Local Lab** — `local-lab/`, a genuinely interactive local simulation of the architecture's rule logic, usable before any Huawei Cloud account exists.

Everything else in the repository (`evidence/`, `simulations/`, `checklists/`, `dashboard/`, `reports/`, `assets/`) supports one of these three layers rather than being a fourth thing.

## Where this project stands right now

Layers 1 and 2 are complete as *designs* — fully specified, internally consistent, and reviewed against general best practice. Layer 3 is complete and actually runs. What hasn't happened yet is deploying Layer 1 to a real Huawei Cloud account and using that live deployment to generate real evidence for Layer 2's validation framework.

## The five execution stages from here

### Stage 1 — Local verification (available now, no Huawei Cloud needed)

```bash
cd local-lab/backend
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` and run every test. Confirm the simulator behaves as documented — this is the fastest way to sanity-check the rule logic in this repository before touching a real cloud account.

### Stage 2 — Improve the local lab (optional, incremental)

Beyond the fixed T-001–T-010 tests, `local-lab/` also includes a small set of **generalized rule testers** — Network, Firewall, Security Group, and Monitoring — where you supply arbitrary inputs (a source IP and port, a CPU/memory/disk percentage) and get a genuinely computed ALLOWED/BLOCKED or NORMAL/ALERT result. See [`../local-lab/README.md`](../local-lab/README.md) for how to use them. This makes the local lab function as a small standalone rule-testing tool, not just a fixed replay of ten scenarios.

### Stage 3 — Try Huawei Cloud

Provision a Huawei Cloud account (checking current free-tier/trial eligibility) and actually build the architecture described in `docs/architecture.md` and `docs/deployment-guide.md`. This is the step that turns Layer 1 from a design into a real environment.

### Stage 4 — Connect the evidence

For each test in `validation/test-register.md`, run it for real against the live account, capture the screenshot or log, and fill in the matching template under `evidence/`. Update that test's status from "Designed — pending deployment" to a real PASS, FAIL, or PARTIAL. For example:

```
T-001 (Unauthorized SSH)
        │
        ▼
Run against live Huawei Cloud
        │
        ▼
Observe actual result
        │
        ▼
Capture screenshot
        │
        ▼
Fill in evidence/Security-Groups/EV-SG-01
        │
        ▼
Update validation/control-matrix.md and validation/test-register.md
        │
        ▼
Re-run risk/risk-assessment.md with validated (not projected) residual risk
```

Once every test in the register has a real result, `docs/design-baseline-score.md` should be retired in favor of a **Validated Security Posture Score**, computed only from real outcomes.

### Stage 5 — Optional live dashboard integration

Only after Stage 4 is substantially complete would connecting `dashboard/` to real Huawei Cloud data (via the SDK-backed approach sketched in `dashboard/backend/README.md`) make sense. This is explicitly the last step, not a shortcut to take instead of Stages 3–4 — a live-looking dashboard with no real evidence behind it would be worse than the current honest static one.

## What changes and what doesn't, once Huawei Cloud access happens

The repository structure doesn't need to be rebuilt. The same files get updated in place:

| Placeholder today | Becomes |
|---|---|
| `Designed — pending deployment` | `Deployed`, then `Tested` |
| Test register status: `Designed` | `PASS` / `FAIL` / `PARTIAL` |
| `evidence/*/EV-*.md` observed-result fields | Real screenshots and logs |
| `docs/design-baseline-score.md` (87/100, design completeness) | `docs/validated-security-posture-score.md` (real score, from real tests) |
| Projected residual risk in `risk/risk-assessment.md` | Validated residual risk |

Nothing here requires new folders, new architecture, or a rewrite — just replacing honest placeholders with real results, one test at a time.
