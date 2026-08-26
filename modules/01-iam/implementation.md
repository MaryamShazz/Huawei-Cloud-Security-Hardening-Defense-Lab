# Implementation Detail — IAM

1. Create four groups: `admins`, `developers`, `operators`, `auditors`.
2. Attach a scoped policy to each group (see `permission-matrix.md` for what each group can and can't do).
3. Enable MFA enforcement at the account level so console login is blocked without a valid MFA code.
4. Set the password policy: 12-character minimum, mixed case + number + symbol required, 90-day rotation, 5-attempt lockout.
5. Add individual users to the group matching their role — never attach a policy directly to a user.
6. Run a permission review: for each group, list what it can actually do and confirm it matches the role it's meant for. Trim anything broader.

Reference config template: [`configs/iam/group-policy-template.json`](../../configs/iam/group-policy-template.json), [`configs/iam/password-policy-template.json`](../../configs/iam/password-policy-template.json).
