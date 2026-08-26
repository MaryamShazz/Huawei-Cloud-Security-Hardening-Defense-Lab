# Implementation Detail — Backup & Recovery

1. Configure a recurring snapshot schedule for all ECS instances.
2. Set a retention policy for how many snapshot generations to keep.
3. Document the restore procedure step by step, before it's needed for real.
4. Perform a test restore to a new, isolated test instance.
5. Verify data integrity on the restored instance against the source.

Full test record: `restore-test.md` in this folder.
