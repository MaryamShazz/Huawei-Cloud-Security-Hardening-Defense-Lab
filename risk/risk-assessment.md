# Risk Assessment

*No live Huawei Cloud environment has been deployed yet.* This rates the threats identified in [`docs/threat-model.md`](../docs/threat-model.md) against the mitigations designed for this project, not mitigations verified in a live account. The "Residual Risk" column below is a projected residual risk after implementing the proposed controls not a measured result from an actual environment, it will become a validated measurement once the controls are deployed and the corresponding tests in [`../validation/test-register.md`](../validation/test-register.md) are actually run. Anything projected at Medium or higher after mitigation is tracked in detail in [`residual-risk-register.md`](residual-risk-register.md) rather than left as a single line item here.

## Methodology

Each risk below was rated by likely impact if it occurred and the likelihood of it occurring in an unhardened environment, then mapped to the mitigation designed for this project. Projected residual risk reflects what would likely be left after the mitigation is deployed and working as intended, not zero in most cases, since no control is absolute.

## Risk Table

| Risk | Impact | Likelihood | Designed Mitigation | Projected Residual Risk |
|---|---|---|---|---|
| Weak or shared IAM credentials | High | Medium | MFA enforced, group-based least privilege | Low |
| Security group open to the internet on an admin port | High | High | Default deny groups, SSH restricted to bastion | Low |
| No audit trail for configuration changes | Medium | High | Cloud Trace Service enabled account wide | Low |
| Publicly accessible storage bucket | High | Medium | Private by default buckets, signed URLs for sharing | Low |
| Undetected resource compromise | High | Medium | Cloud Eye monitoring with alert thresholds | Medium |
| Untested backup/recovery process | Medium | Medium | Scheduled snapshots planned, restore procedure documented (not yet executed) | Medium |
| Lateral movement between instances | High | Medium | Public/private subnet split, tiered security groups | Low |
| Unpatched instance software | Medium | Medium | Patch schedule as part of hardening checklist | Medium |
| Alert fatigue from poorly tuned thresholds | Low | Medium | Thresholds set from initial baseline, flagged for review | Medium |

## Notes on residual risk

A few items sit at "Medium" projected residual risk rather than "Low" because they depend on things that can't be evaluated without real production traffic or a live incident: monitoring thresholds, patch cadence over time, and how well the recovery process holds up under actual pressure rather than a single planned test run. These are the same items flagged as open follow-up work in `checklists/security-review.md`. All of these ratings, including the "Low" ones, are projections based on the design working as intended, none have been confirmed against a live Huawei Cloud account yet.

## Priority for follow-up

1. Deploy the design to a live Huawei Cloud account and execute the tests in `validation/test-register.md`, converting each projected residual risk rating into a validated one.
2. Tune monitoring thresholds once real traffic data is available.
3. Run a tabletop incident response exercise to test detection and containment under simulated conditions.
4. Establish a recurring patch cadence rather than a one time pass.
