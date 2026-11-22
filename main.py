#!/usr/bin/env python3
"""Write a short, calming text for the AI judge to /output/entry.txt."""

from pathlib import Path

TEXT = (
    "The evening rain has softened to a hush on the roof. A mug of tea "
    "rests warm between two palms, in no hurry to be finished. A blanket "
    "waits folded nearby, and down the hall a small lamp stays on, so "
    "the night does not have to sit alone."
)


def main() -> None:
    # Self-check: the entry must be 1-280 Unicode characters, not blank.
    if not (1 <= len(TEXT) <= 280) or not TEXT.strip():
        raise ValueError(f"entry text out of bounds: {len(TEXT)} characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
