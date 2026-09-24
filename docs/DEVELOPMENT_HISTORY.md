# Development history

This project predates its Git repository. The first Git commit is a truthful snapshot of the surviving audited R3 artifact. No commits were backdated or synthesized to represent earlier work.

## Pre-Git milestones

The order below is reconstructed from surviving project records and verified source bytes. It documents pre-Git development; it is not reconstructed Git history.

| Milestone | Outcome |
| --- | --- |
| Standalone guard | Real-SFM testing established successful startup cancellation and confirmed that a later intentional Workshop removal window remained usable in the same session. |
| Lifecycle continuity | Python wrapper identity and weak references were unsuitable for proving continuity across polling callbacks. The qualified guard therefore uses a retained QObject lifecycle sentinel, invalidated by terminal lifecycle events. QPointer and Shiboken pointer access were unavailable in the tested SFM build. |
| Conservative target handling | The guard was narrowed to `QApplication.activeModalWidget()`, exact title and widget-structure checks, two stable positive samples, one cancellation attempt, and fail-closed behavior. Broad top-level widget enumeration was rejected after causing a native SFM crash during testing. |
| Eligible startup budget | Runtime timing showed the Workshop cleanup prompt appears after startup becomes unblocked. The final guard therefore uses 40 seconds of accumulated eligible polling time rather than a simple wall-clock deadline; unrelated application-modal windows pause that budget. |
| Single-file dual-host architecture | The wrapper isolates persistent implementation state from loader globals so retained callbacks remain stable and duplicate invocation does not reset an active or completed guard. Filesystem self-location was avoided. |
| First dual-host implementation | Review identified unsafe retry behavior after timer-start failure, a later install exception that could remain retryable, and an allocation failure that could strand bootstrap state. |
| R2 | Added conservative pristine-state retry classification, `RETRYING_INSTALL`, and identity-checked pre-execution cleanup. The nested helper then exposed Python 2.7.5's tuple-form `exec` compilation restriction. |
| R3 | Replaced only the outer tuple-form `exec` operation with evaluation of an already-compiled exec-mode code object and updated the adjacent comment. Full-file Python 2.7.5 compilation and isolated checks passed. The resulting gate was readiness for real-SFM qualification, not proof that every R3 entry route had been exercised live. |
| Git publication | The repository began with the surviving R3 artifact as its truthful first commit. A later preparation commit added documentation, tests, licensing, and deterministic packaging without changing the R3 production source. |

## Byte authority

Authoritative R3 source, distributed here as `Remove_Remove_Workshop_Prompt.py`:

```text
bytes: 48019
sha256: 06c6654df735849fcd5ea4d3c437107ad358a23ba04c0a114fd902b0b9130356
```

Embedded qualified guard:

```text
bytes: 25077
sha256: 078555ae2b93e01462e40c019ca862dcb65ddf55c790e234e468b5832c838bfa
```

Authority is based on the R3 verification record, the exact R2-to-R3 delta, and matching bytes across surviving source and distributed copies. File timestamps or installation location alone were not used to choose the source. The older standalone artifact remains the protected embedded component, not a competing current launcher.

The first committed blob and audited R3 source both contain 1,107 LF bytes, zero CR bytes, and the same SHA-256. The embedded body contains 889 LF bytes, zero CR bytes, and its original final newline. Repository attributes prevent Git from converting the production artifact's bytes on checkout.

## Public evidence boundary

The production artifact, durable source-based conclusions, and portable verification tests are retained publicly. Raw development evidence is intentionally excluded from the public repository. The public documentation records the conclusions needed to maintain the project without exposing unnecessary development material.
