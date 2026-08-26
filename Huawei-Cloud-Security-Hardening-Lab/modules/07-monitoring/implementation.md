# Implementation Detail — Monitoring (Cloud Eye)

1. Enable Cloud Eye on every ECS instance.
2. Configure CPU, memory, and disk utilization alerts at 85%, 90%, and 85% respectively, evaluated over multiple consecutive periods to avoid single-spike false positives.
3. Connect the alert action to a real notification channel (webhook, email, or equivalent).
4. Send a synthetic load to a test instance to confirm the alert actually fires and reaches the notification channel.
5. Flag thresholds for retuning once real production traffic data is available — this is tracked explicitly in `risk/residual-risk-register.md` (RR-01).

Reference: [`configs/monitoring/alert-baseline.md`](../../configs/monitoring/alert-baseline.md) and [`configs/monitoring/cloud-eye-thresholds-template.json`](../../configs/monitoring/cloud-eye-thresholds-template.json).
