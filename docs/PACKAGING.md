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

Earlier R3 packages placed the correct script bytes beneath `workshop/scripts/sfm/` while their README described a `usermod` installation. The current builder corrects that distribution mismatch without changing the production script.

The builder uses an explicit allowlist, checks the complete R3 hash, rejects symlink inputs and a conflicting existing output, fixes archive order, timestamps and attributes, and uses stored entries so compression-library versions do not affect the bytes. An identical existing output is accepted. It verifies the archive payload and CRCs before returning its size and digest.

Determinism requires the same input file bytes and builder. Documentation changes deliberately change the archive digest. The license and README are package documentation, not additional executable Workshop scripts: the runnable tool remains one `.py`.

## Published v1.0.1 provenance

The annotated tag `v1.0.1` points to commit:

```text
4895ff513171e32279bb6e826e5e839e2a7eaee3
```

Published release asset:

```text
Remove-Remove-Workshop-Prompt-v1.0.1.zip
bytes: 58962
sha256: 52184637dc457cd784a459689eade27bfc2b7811fb720d8c359f8773e041dbd9
```

The release tag and asset are historical release provenance. Documentation cleanup after v1.0.1 does not move the tag or replace the asset.

A GitHub source archive is a separate artifact and is not an install-ready replacement for the manual-install layout.
