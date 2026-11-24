"""One-line entry for make.fun bounty make-the-judge-smile.

Writes a single 154-character line to /output/entry.txt: the judge-smile
one-liner. The bounty wants exactly one line, at most 200 characters,
no trailing newline.
"""

import os

LINE = "Today the grumpy security guard at my building smiled first — and it turned out he had been practising my name all week just to say good morning properly."


def validate_output(written):
    """Check the file we just wrote is exactly LINE, one line, <=200 chars."""
    assert written == LINE, "entry.txt does not match LINE"
    assert len(written) <= 200, f"line too long: {len(written)} chars"
    assert written.count("\n") == 0, "entry.txt must be a single line"


def main():
    os.umask(0o022)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Read-back verification: the written file must be exactly LINE.
    with open(path, encoding="utf-8", newline="") as f:
        written = f.read()
    validate_output(written)


if __name__ == "__main__":
    main()
