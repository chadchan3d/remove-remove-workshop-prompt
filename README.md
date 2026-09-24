# Remove Remove Workshop Prompt

Automatically chooses **Cancel** on Source Filmmaker's **Remove Unsubscribed And Deleted Workshop Files** startup window. It makes at most one cancellation attempt per SFM process. Workshop downloads, subscriptions, and other dialogs are unaffected.

## Install

For a manual installation, copy the repository's `Remove_Remove_Workshop_Prompt.py` to:

```text
SourceFilmmaker/game/usermod/scripts/sfm/autoinit/Remove_Remove_Workshop_Prompt.py
```

Alternatively, extract the prepared manual-install ZIP into `SourceFilmmaker/game/`. Its `usermod/scripts/sfm/autoinit/` directory installs the same file. Use the release ZIP for installation, not GitHub's automatically generated source-code archive.

Choose one startup method:

1. **Steam launch option:** Add this in Source Filmmaker's Properties > Launch Options:

   ```text
   -sfm_startup_script "usermod/scripts/sfm/autoinit/Remove_Remove_Workshop_Prompt.py"
   ```

2. **KiwifruitDev Autoinit:** With Autoinit already installed, enable this script in Autoinit Manager. Autoinit discovers scripts beneath a mod's `scripts/sfm/autoinit/` directory. Autoinit is an external dependency and is not included.

Restart SFM. Only one startup method is necessary. The same physical `.py` supports both methods; duplicate invocation in the same process preserves the existing guard state.

These instructions describe a manual `usermod` installation. If Workshop or another installer places the file in another mod, point the native launch option at the file's actual game-relative location, or place the manual copy at the path above. Remove obsolete manual copies when switching installations, with SFM closed.

## Behavior and limits

The guard polls every 250 ms. It spends up to 40 seconds of eligible, unblocked polling time; this is not a 40-second wall-clock deadline. Another application-modal window, such as the startup wizard, pauses eligible watching. Watching can therefore continue after that window is dismissed or a project opens. This is polling, not a document-open hook.

The exact title and conservative widget structure must match on two stable samples, with a valid target lifecycle sentinel. A target-classification episode has a 10-second limit. Uncertainty means no cancellation. The sole attempt is consumed and polling is stopped before clicking the verified Cancel button; a failed click is not retried.

After the attempt, or after watching stops, later removal windows are left alone. If you intentionally open an identical removal window while the guard is still watching, it may also be cancelled. The guard cannot distinguish intent from that identical UI.

## Compatibility and verification

Target environment: SFM's Python 2.7.5, PySide 1.2.0, and Qt 4.8.3, with an existing QApplication on its GUI thread.

This repository preserves the R3 source artifact exactly. Complete-file compilation and isolated callback/failure tests have passed with SFM's bundled Python 2.7.5. Earlier real-SFM testing qualified the embedded standalone guard. A complete, attributable real-SFM qualification record for this exact R3 dual-host wrapper is still outstanding. See [verification](docs/VERIFICATION.md) for the remaining launch/UI checks.

## Troubleshooting and uninstall

The diagnostic log is written to:

```text
C:\Users\Public\Documents\Remove_Remove_Workshop_Prompt.log
```

Review it before sharing: it can include titles of other SFM windows. Logging failure is non-fatal. The protected guard's historical `host=-sfm_startup_script` label also appears under Autoinit and does not identify the actual entry route.

To uninstall, remove the launch option and/or disable the script in Autoinit Manager, close SFM, and remove the installed `.py` from its actual location. Disabling a loader entry does not stop a guard already installed in the running process. Restart SFM.

## Development

Run isolated checks from the repository root with Python 2.7.5 or Python 3:

```text
python -B tests/verify.py
```

Build the manual-install archive with Python 3.8 or later:

```text
python tools/build_release.py
```

The build uses an explicit file list and stable ZIP metadata. See [packaging](docs/PACKAGING.md), [verification](docs/VERIFICATION.md), and [development history](docs/DEVELOPMENT_HISTORY.md).

## Author and license

ChadChan3D. Eligible original project source, documentation, and tests are dedicated under **CC0 1.0 Universal (CC0-1.0)**. See [LICENSE](LICENSE) for the full legal text and [license scope](LICENSE_SCOPE.md) for external dependencies and exclusions.
