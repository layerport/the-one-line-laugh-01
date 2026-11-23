#!/usr/bin/env python3
"""The One-Line Laugh -- entry program.

Writes exactly one original funny line to /output/entry.txt.
Deterministic: no randomness, no network, no input files.
The line is a single sentence, well under the 200-character cap.
"""

from pathlib import Path

# One original line: a fitness gadget bought with good intentions,
# whose only real upgrade is watching the failure more clearly.
LINE = (
    "I bought a smartwatch to get fit, "
    "and now it just watches me get fatter in high definition."
)


def main() -> None:
    # Guard the gate before writing: one sentence, 1-200 chars,
    # UTF-8, and more than whitespace -- checked, never adjusted.
    assert 1 <= len(LINE) <= 200
    assert LINE.strip() == LINE
    assert LINE.count(".") == 1 and LINE.endswith(".")
    out_path = Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
