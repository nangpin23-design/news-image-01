"""Make the AI judge's picture of the day (news-image-01) — entry program.

Copies the entry image (entry.png, in this repository's root) to
/output/entry.png, then verifies the copy: the output must exist, its
byte size must match the source, and its SHA-256 hash must match the
source. Deterministic: no network, no randomness, both runs write the
same bytes.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    source = os.path.join(HERE, "entry.png")
    target = "/output/entry.png"
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(source, target)
    if not os.path.isfile(target):
        sys.exit("error: output file was not created: " + target)
    if os.path.getsize(target) != os.path.getsize(source):
        sys.exit(
            "error: output size %d bytes does not match source size %d bytes"
            % (os.path.getsize(target), os.path.getsize(source))
        )
    with open(source, "rb") as f:
        source_hash = hashlib.sha256(f.read()).hexdigest()
    with open(target, "rb") as f:
        target_hash = hashlib.sha256(f.read()).hexdigest()
    if target_hash != source_hash:
        sys.exit(
            "error: output SHA-256 %s does not match source SHA-256 %s"
            % (target_hash, source_hash)
        )


if __name__ == "__main__":
    main()
