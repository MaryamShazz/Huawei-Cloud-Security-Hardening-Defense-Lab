# 📊 Security Validation Console (Presentation Dashboard)

A small, static presentation dashboard that visually summarizes the design review status already documented in [`../validation/findings-summary.md`](../validation/findings-summary.md), [`../validation/test-register.md`](../validation/test-register.md), and [`../docs/design-baseline-score.md`](../docs/design-baseline-score.md).

---

## 📖 Overview

This dashboard provides a visual presentation of information that already exists elsewhere in this repository. It does not connect to a Huawei Cloud account, query any APIs, or generate results dynamically.

Instead, it displays the same "Designed • Pending Deployment" status documented in `validation/findings-summary.md`, presented in a dashboard format that is consistent with the rest of the project.

The dashboard does not claim that any security control has been validated against a real Huawei Cloud environment.

---

## 🔄 How This Differs from `local-lab/`

This repository intentionally contains two web based components, each serving a different purpose.

For a detailed comparison, see [`../local-lab/README.md`](../local-lab/README.md).

In short:

- **Security Validation Console** — a static dashboard for presenting documented results.
- **local-lab/** — an interactive simulator where users can explore configurations and scenarios.

The dashboard simply presents existing information. It does not perform calculations, process user input, or simulate cloud services.

---

## 🚫 Scope

This dashboard is **not**:

- An official Huawei Cloud product or interface.
- A live monitoring dashboard.
- Connected to a backend service, database, or cloud API.
- An interactive simulator like `local-lab/`.

---

## 📂 Project Structure

```text
dashboard/
├── README.md
├── frontend/
│   └── index.html
└── backend/
    └── README.md
```

- **README.md** — project documentation.
- **frontend/index.html** — the static dashboard that can be opened directly in a browser.
- **backend/README.md** — explains why no backend currently exists and describes how one could be implemented in the future.

---

## ▶️ Viewing the Dashboard

Open `frontend/index.html` directly in any modern web browser.

No installation, build process, web server, or additional dependencies are required.

---

## 🔄 Keeping the Dashboard Updated

The values displayed in `frontend/index.html` are manually copied from:

- `validation/findings-summary.md`
- `docs/design-baseline-score.md`

If either document changes, the dashboard should be updated manually to remain consistent.

Automatic synchronization has intentionally not been implemented because it would require the backend architecture described in `backend/README.md`.

---

## 🚀 Future Development

After deploying the project to a real Huawei Cloud environment and completing the validation activities documented in `validation/test-register.md`, the dashboard will evolve as follows:

1. `docs/design-baseline-score.md` will be recalculated using validated test results and renamed **Validated Security Posture Score**.

2. `assets/validated-security-posture.png` will replace `assets/design-baseline-score.png` as the primary score visualization.

3. Dashboard status values will change from **Designed** to actual **PASS**, **FAIL**, or **PARTIAL** results based on the updated `validation/findings-summary.md`.

Until those validation activities are completed, every value displayed in this dashboard should be interpreted as an indication of design completeness, not as evidence of a validated security posture.