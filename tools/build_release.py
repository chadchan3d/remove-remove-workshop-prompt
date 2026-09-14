"""Build the explicit, deterministic R3 manual-install archive (Python 3.8+)."""
import argparse
import hashlib
import io
from pathlib import Path
import zipfile

SOURCE_HASH = '06c6654df735849fcd5ea4d3c437107ad358a23ba04c0a114fd902b0b9130356'
FILES = (
    ('release/README.txt', 'README.txt'),
    ('LICENSE', 'LICENSE'),
    ('LICENSE_SCOPE.md', 'LICENSE_SCOPE.md'),
    ('Remove_Remove_Workshop_Prompt.py', 'usermod/scripts/sfm/autoinit/Remove_Remove_Workshop_Prompt.py'),
)

def build(root):
    payloads = {}
    for local, archive in FILES:
        path = root / local
        if path.is_symlink() or not path.is_file():
            raise ValueError('Missing or symlink input: ' + local)
        payloads[archive] = path.read_bytes()
    source = payloads[FILES[-1][1]]
    if len(source) != 48019 or hashlib.sha256(source).hexdigest() != SOURCE_HASH:
        raise ValueError('Production source differs from the audited R3 artifact')
    output = io.BytesIO()
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_STORED) as archive:
        for _, name in FILES:
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, payloads[name])
    data = output.getvalue()
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        assert archive.namelist() == [name for _, name in FILES]
        assert archive.testzip() is None
        assert all(archive.read(name) == contents for name, contents in payloads.items())
    return data

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    destination = args.output or root / 'dist' / 'Remove_Remove_Workshop_Prompt_R3_manual.zip'
    data = build(root)
    assert data == build(root), 'Repeated build differed'
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        if destination.is_symlink() or destination.read_bytes() != data:
            raise ValueError('Output already exists with different bytes; choose a new output path')
    else:
        with destination.open('xb') as handle:
            handle.write(data)
    print(destination.name)
    print('bytes: ' + str(len(data)))
    print('sha256: ' + hashlib.sha256(data).hexdigest())

if __name__ == '__main__':
    main()
