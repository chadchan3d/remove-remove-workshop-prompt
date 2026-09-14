"""Check deterministic packaging and exclusion/error boundaries; Python 3.8+."""
import importlib.util
import io
from pathlib import Path
import shutil
import tempfile
import zipfile

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('release_builder', root / 'tools/build_release.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
first = builder.build(root)
assert first == builder.build(root)
with zipfile.ZipFile(io.BytesIO(first)) as archive:
    assert archive.namelist() == ['README.txt', 'LICENSE', 'LICENSE_SCOPE.md',
        'usermod/scripts/sfm/autoinit/Remove_Remove_Workshop_Prompt.py']
    assert archive.read(archive.namelist()[-1]) == (root/'Remove_Remove_Workshop_Prompt.py').read_bytes()
    assert archive.testzip() is None
with tempfile.TemporaryDirectory(prefix='rrwp-package-test-') as directory:
    fixture = Path(directory)
    for local, unused in builder.FILES:
        destination = fixture/local
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root/local, destination)
    (fixture/'unselected.log').write_text('Not a release input')
    assert builder.build(fixture) == first
    (fixture/'Remove_Remove_Workshop_Prompt.py').write_bytes(b'# stale source\n')
    try:
        builder.build(fixture)
    except ValueError:
        pass
    else:
        raise AssertionError('Stale source was accepted')
print('Packaging verified: deterministic bytes, exact layout, exclusions, stale-source rejection')
