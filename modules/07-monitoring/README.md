# 07 — Monitoring (Cloud Eye)

## Objective
Detect abnormal resource behavior before it becomes an incident.

## Why It Matters
Logging tells you what happened after the fact. Monitoring is what actually raises a flag while something is happening.

## Configuration
- Cloud Eye enabled on all ECS instances
- Alert thresholds: CPU 85%, memory 90%, disk 85%, evaluated over multiple consecutive periods
- Notification channel confirmed reachable

See [`configs/monitoring/`](../../configs/monitoring/) for the threshold template.

## Screenshots
See [`screenshots/monitoring/`](../../screenshots/monitoring/).

## Security Benefit
Surfaces resource compromise (cryptomining, DoS, runaway processes) that wouldn't necessarily show up in an audit log.

## Best Practices
Tune thresholds against actual observed traffic once available — an initial estimate is a starting point, not a final answer.

## Security Engineer's Notes
**Status: thresholds are an initial estimate, flagged in `risk/residual-risk-register.md` (RR-01) as pending real-traffic tuning.**

## Further Detail
Step-by-step implementation notes: [`implementation.md`](implementation.md). Screenshots: [`screenshots/`](screenshots/).
