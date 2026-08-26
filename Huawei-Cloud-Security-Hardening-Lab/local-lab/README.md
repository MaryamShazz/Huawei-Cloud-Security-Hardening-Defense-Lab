# Local Lab

A small, genuinely runnable local application that implements a **rule-based local security validation simulator, based on this project's designed Huawei Cloud security architecture** — not a Huawei Cloud emulator and not a reproduction of any real Huawei Cloud API. You can open and run this the same way you'd run the SOC dashboard or FYP project: start a real local server, open a real browser tab, click a button, get a real (if simulated) result.

**How to describe this project accurately, if you're presenting it:** call it a *"local security validation simulator based on the project's Huawei Cloud security architecture."* Avoid describing it as *"a simulated Huawei Cloud environment,"* since that phrasing implies it reproduces actual Huawei Cloud services or APIs, which it does not — it evaluates a simplified rule model of the same logic, in plain Python, with no Huawei SDK involved anywhere.

## How this differs from `dashboard/`

This repository has two separate small web things, and they intentionally do different jobs:

| | `local-lab/` | `dashboard/` |
|---|---|---|
| Job | Interactive — you provide input, the simulator evaluates a rule, you get a result | Presentation — shows the existing design review status and score at a glance |
| Data | Computed live by `backend/app.py` on every click | Hand-copied from `validation/findings-summary.md` and `docs/design-baseline-score.md` |
| Backend | Real Flask app, real logic | None — static HTML only |
| Can the output change? | Yes — change the input, get a different real result | No — it's a snapshot until someone edits the HTML |

If you're looking for something to click around in and test rules against, use `local-lab/`. If you're looking for a clean visual summary to show someone, use `dashboard/`.

## What this is

Real Python code (`backend/app.py`) evaluating a simplified rule model of this environment's architecture: an admin IP allow-list for the bastion, a firewall deny-list, tiered security group logic, and a Cloud Eye-style CPU threshold check. When you run a test, the backend actually evaluates your input against those rules and returns a real result — change the source IP on the SSH test and you'll get a different, genuinely computed answer, not a scripted one.

## What this is not

**Not connected to Huawei Cloud in any way.** There is no live mode in this build. Every result is labeled `LOCAL SIMULATION` in the UI and in the API response. This is a model of the architecture for demonstration and testing-the-logic purposes, not a substitute for actually deploying to Huawei Cloud and running the real tests in [`../validation/test-register.md`](../validation/test-register.md).

## Requirements

- Python 3.9+
- Flask (`pip install -r backend/requirements.txt`)

## Run it

```bash
cd local-lab/backend
pip install -r requirements.txt
python app.py
```

Then open **http://localhost:5000** in a browser.

## What you can do

- Click "Run Test" on any of the ten cards (T-001 through T-010) to execute that test against the local rule model.
- For T-001 (unauthorized SSH) and T-005 (firewall deny-list), edit the source IP field before running to see the outcome actually change based on whether that IP falls inside the relevant range.
- For T-008 (Cloud Eye threshold), edit the CPU percentage to see the alert logic cross (or not cross) the configured threshold.
- Use the four **Generalized Rule Testers** below the fixed test cards — Network, Firewall, Security Group, and Monitoring — to supply your own arbitrary input (any source IP, any tier pair, any CPU/memory/disk combination) and get a genuinely computed result, rather than replaying one of the ten fixed scenarios. These correspond to Stage 2 of [`../docs/execution-roadmap.md`](../docs/execution-roadmap.md).
- Watch the event log at the bottom populate in real time as you run tests, each one timestamped and tagged `LOCAL SIMULATION`.
- T-010 (incident response tabletop) will always return "not applicable" — this one genuinely can't be simulated by code, and the UI says so rather than faking a result.

## How this relates to the rest of the repository

Results here are **not** written back into [`../validation/test-register.md`](../validation/test-register.md) or [`../validation/validation-results.md`](../validation/validation-results.md), which track the actual live-deployment status (currently "Designed — pending deployment" for everything). This local lab exists to make the project demonstrable and interactive before a live Huawei Cloud account is available, not to substitute for the real evidence that only a live deployment can produce.

## Extending it

The rule model in `backend/app.py` is intentionally simple and self-contained (in-memory Python, no database, no external calls). If you deploy the real environment to Huawei Cloud later, the natural next step is the live-mode integration sketched in [`../dashboard/backend/README.md`](../dashboard/backend/README.md) — a genuinely separate piece of work, not an extension of this simulator, since it would need real Huawei Cloud SDK credentials and API calls rather than the local rule model used here.
