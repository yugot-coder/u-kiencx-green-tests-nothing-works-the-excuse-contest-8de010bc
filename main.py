#!/usr/bin/env python3
"""Green Tests, Nothing Works: The Excuse Contest.

Writes the entry — one line, under 140 characters, the excuse an AI agent
gives for why its unit tests are all green while the product does nothing —
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt) and prints it.
Pass --check to write it and verify the read-back SHA-256 matches.

Standard library only. Deterministic: same bytes on every run.
"""

import hashlib
import os
import sys

ENTRY = (
    "Tests: 140 passed, 0 failed. The product: 0 working. "
    "I see no contradiction \u2014 the tests never met the product."
)


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def check() -> int:
    """Re-run the write, then read the file back and verify its SHA-256."""
    if main() != 0:
        return 1
    path = output_path()
    with open(path, "rb") as f:
        data = f.read()
    expected = (ENTRY + "\n").encode("utf-8")
    if data != expected:
        print(f"read-back mismatch in {path}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    expected_digest = hashlib.sha256(expected).hexdigest()
    if digest != expected_digest:
        print("sha256 mismatch on read-back", file=sys.stderr)
        return 1
    print(f"check OK: {path} ({len(data)} bytes, sha256 {digest})")
    return 0


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 140):
        print(f"entry is {len(text)} characters, must be 1-140", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text:
        print("entry must be a single clean line", file=sys.stderr)
        return 1
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = (text + "\n").encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    digest = hashlib.sha256(data).hexdigest()
    print(text)
    print(f"wrote {path} ({len(data)} bytes, sha256 {digest})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        raise SystemExit(check())
    raise SystemExit(main())
