#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- make.fun entry.

Writes exactly one letter to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output/entry.txt when the variable is unset):
"A" for coffee. Nothing else -- no word, no explanation, no punctuation.

Why coffee: of the two drinks, coffee is the bolder, more vivid answer --
the smell that wakes a house, the cup people reach for before they can
form a sentence. Tea soothes; coffee declares. One letter, "A", says it.
"""

import os

LETTER = "A"  # A = coffee (B would be tea).


def main():
    # An empty MAKEFUN_OUTPUT_DIR is the same as unset: fall back to /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one byte, "A": no newline, no trailing space, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
