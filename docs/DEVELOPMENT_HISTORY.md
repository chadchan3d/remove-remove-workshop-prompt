# Development history

This project predates its Git repository. The first Git commit is a truthful snapshot of the surviving audited R3 artifact. No commits have been backdated or synthesized to represent the earlier work.

## Preserved milestones

The following order is reconstructed from project review records and verified source bytes. Review dates describe records, not inferred dates for individual SFM experiments.

| Milestone | Evidence and outcome |
| --- | --- |
| Standalone guard | The September 10, 2026 handoff identifies an already-qualified standalone guard. It reports lifecycle experiments and successful startup cancellation, followed by a usable intentional removal window. These are retained project reports; the raw original runtime logs are not packaged here. |
| Lifecycle continuity | Earlier attempts using Python wrapper identity or weak references were replaced with a retained QObject sentinel. Source inspection confirms the final event-filter and terminal-signal approach. Reports of absent QPointer/Shiboken APIs apply to the tested SFM build only. |
| Single-file dual-host architecture | The supplied Autoinit loader executes discovered scripts in its shared globals. Review selected an embedded private implementation namespace to keep retained callbacks independent of later host assignments. Filesystem self-location was avoided. |
| First dual-host implementation | Review found unsafe repeated installation after a caught timer-start failure, an unlatching later install exception, and an allocation failure stranded in LOADING. |
| R2 | Added conservative pristine-state retry classification, RETRYING_INSTALL, and identity-checked pre-execution cleanup. These fixed the three state issues. The nested helper exposed Python 2.7.5's tuple-form exec compilation restriction. |
| R3 | Replaced only the outer tuple-form exec operation with eval of an already-compiled exec-mode code object and updated the adjacent comment. Independent full-file Python 2.7.5 compilation and isolated checks passed. The gate verdict was readiness for real-SFM qualification, not proof of completion of that qualification. |
| Publication preparation | Preserves R3 bytes, documents provenance, makes the tests portable, and corrects manual archive paths. The new repository preserves the genuine first commit rather than manufacturing development history. |

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

Authority is based on the R3 verification record, the final review, the exact R2-to-R3 delta, and matching bytes across the surviving loose, archive-payload, and installed copies. File timestamps or installation location alone were not used to choose the source. The older standalone artifact remains the protected embedded component, not a competing current launcher.

The first committed blob and original working file were compared directly with R3: both have 1,107 LF bytes, zero CR bytes, and the same SHA-256. The embedded body has 889 LF bytes, zero CR bytes, and its original final newline. The new attributes prevent Git from converting the production artifact's bytes on checkout.

## Evidence disposition

The production artifact is retained exactly. Durable source-based conclusions and newly rerun portable tests are retained publicly. Original handoffs, machine-specific harnesses, older development probes, release archives, and third-party reference files remain outside this publication candidate at their existing locations; this preparation neither deletes them nor republishes them. The public records do not expose private storage locations. A sanitized knowledge package is maintained separately from the project repository.
