# Manual-install packaging

Run `python tools/build_release.py` with Python 3.8 or later. Output defaults to `dist/Remove_Remove_Workshop_Prompt_R3_manual.zip`.

Exact archive contents:

```text
README.txt
LICENSE
LICENSE_SCOPE.md
usermod/scripts/sfm/autoinit/Remove_Remove_Workshop_Prompt.py
```

Extract into the SFM `game` directory. The documented native launch option and Autoinit discovery then use the same physical file. This is a manual-install archive, not a statement about Steam Workshop's mounting or uploader behavior.

Older R3 ZIPs carried the correct script bytes beneath `workshop/scripts/sfm/` while describing a different `usermod` path in their README. This build corrects that distribution mismatch without changing the script. Old ZIPs remain evidence outside the repository; they are not release inputs.

The builder uses an explicit allowlist, checks the complete R3 hash, rejects symlink inputs and a conflicting existing output, fixes archive order, timestamps and attributes, and uses stored entries so compression-library versions do not affect the bytes. An identical existing output is accepted. It verifies the archive payload and CRCs before returning its size and digest. No third-party binary, log, cache, research archive, or Git metadata is collected.

Determinism requires the same input file bytes and builder. Documentation changes deliberately change the archive digest. The license/readme are package documentation, not additional executable Workshop scripts: the runnable tool remains one `.py`.

No release tag or GitHub Release is created by this command. A GitHub source archive is a separate artifact and is not an install-ready replacement for this layout.
