# Verification boundaries and procedure

The public tests are portable adaptations of earlier project-owned isolated harnesses. They are newly rerun checks, not copies of the original SFM experiments. They substitute Qt objects and deny guard log-file access; they never import a real PySide module or launch SFM. The process terminates after the harness runs and discards the fake modules.

## Mechanical checks

`python -B tests/verify.py` checks exact outer/embedded fingerprints, complete compilation, private function globals (including lifecycle closures), host pollution, duplicate invocation, consumed attempts, clean prerequisite retry, failure latches, and pre-execution ownership cleanup. It checks the relevant Autoinit literal rewrite triggers and filename exclusions without redistributing the third-party loader.

Run with SFM's bundled `sdktools/python/2.7/win32/python.exe -B -S tests/verify.py` from this repository to test the actual Python 2.7.5 compiler. A Python 3 result alone cannot establish compatibility with that older compiler. `tests/python275_exec_regression.py` is a small independent reproducer of the R2 compiler restriction and the R3 remedy.

At the original R3 gate, 78 isolated assertions ran with Python 3 and 16 targeted assertions ran with the actual bundled Python 2.7.5. The new portable suite records its own current counts and version. The full R3 artifact and embedded guard are fingerprinted, so publication-only work must not silently replace either.

## Real-SFM status

The prior standalone handoff reports successful lifecycle tracking, Cancel mutation, and a later usable removal window in Python 2.7.5 / PySide 1.2.0 / Qt 4.8.3. Those observations concern the earlier standalone guard and experiments. The same guard bytes are embedded in R3, but that identity does not prove all R3 entry routes were exercised in SFM.

The current publication review did not launch SFM or perform GUI actions. Exact-R3 dual-host UI qualification remains unverified. This limitation is a runtime gate, not evidence of a newly found source defect.

## Minimal real-SFM qualification

Record the installed source SHA-256, environment versions, entry order, and observed result for each fresh process:

1. Autoinit only: confirm discovery, one retained polling timer, and normal target cancellation.
2. Native launch option only: confirm the documented path is opened and the target is cancelled normally.
3. Both entry orders in separate fresh processes: compare implementation/runtime/timer identity before and after the second entry.
4. Manager Run while watching, then after cancellation: budget, sentinel, and consumed attempt must not reset.
5. Observe target lifecycle invalidation and post-action diagnostics; then deliberately open a later removal window and confirm it remains usable.
6. Include loader re-entry or an identical duplicate copy; neither should create another guard. A host-global pollution probe is optional and should be isolated to a controlled test session.

Review logs before sharing. Keep failure injection in the isolated harness. Do not run experimental mutation probes in a production SFM session merely to validate packaging.
