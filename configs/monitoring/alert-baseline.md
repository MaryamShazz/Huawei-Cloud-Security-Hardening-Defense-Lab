# Cloud Eye Alert Baseline

| Metric | Threshold | Evaluation Window | Status |
|---|---|---|---|
| CPU utilization | 85% | 5 min, 3 consecutive periods | Initial estimate — pending real-traffic tuning |
| Memory utilization | 90% | 5 min, 3 consecutive periods | Initial estimate — pending real-traffic tuning |
| Disk utilization | 85% | 10 min, 2 consecutive periods | Initial estimate — pending real-traffic tuning |
| Network inbound | Baseline + margin | 5 min, 2 consecutive periods | Not yet set — requires observed baseline |

These are starting points, not final values. See `risk/residual-risk-register.md` (RR-01) for the plan to revisit them.
