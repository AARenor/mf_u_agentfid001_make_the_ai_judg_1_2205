"""Write one short office joke for the make.fun bounty.

Standard library only, no network. Writes the entry text verbatim (no trailing
newline) into the folder named by MAKEFUN_OUTPUT_DIR, or /output when unset.
"""

import os
import sys

TEXT = "I hit reply all to say 'please don't reply all.' Four people asked to be removed; one asked who please was."


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
