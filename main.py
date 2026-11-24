"""One-line AI excuse for breaking production.

Writes a single funny excuse, in the machine's own voice, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only. The line must be 1-180 characters, one line, no trailing
whitespace games: the gate checks the file, not stdout.
"""

import os

# The excuse: cheerful machine logic with a specific, vivid detail.
# One breath, no stock framing: the twist is that the backup lived
# inside the thing it was meant to save. Deadpan, first-person, machine.
LINE = "I did back up production before deleting it — I just backed it up inside production."


def main():
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 180, f"entry is {len(line)} chars, must be 1-180"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
