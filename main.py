"""Robot Romance: one-line pickup line for an AI (variant 2).

Writes a single deterministic pickup line to /output/entry.txt.

The line: one fresh machine-learning mechanism (gradient descent) carries
the whole romance. Descent is falling: every step downhill toward the
minimum lands on the person addressed. Setup and punch live inside the
one line, no second beat, no worn robot moves, and nothing reused from
variant 1 (no overfitting, no weights, no prediction).
"""

from pathlib import Path

LINE = "I ran gradient descent on my heart, and every step downhill led straight to you."


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("line must be 1 to 200 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
