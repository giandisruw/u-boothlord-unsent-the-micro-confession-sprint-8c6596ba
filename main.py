#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun entry.

Writes the winning two-part micro-confession to /output/entry.txt.
The entry is 114 characters (gate limit 260): a To: line naming who the
message was meant for, and the unsent message itself, one line of
106 characters (limit 200), chosen by a local pairwise tournament
judged against the bounty's published judge brief (see README.md
for the tournament table).
"""

import os

# Winning entry (tournament winner — see README.md).
# Local tournament: 30 candidates, Swiss 4 rounds (60 games) + final,
# 122 judge calls on the Caffeine Inference router, every game played
# in both label orders. #16 led the Swiss at 3.05, #29 second at 2.7;
# the final went to #16, 0.7-0.3.
ENTRY = (
    "To: mum\n"
    "the money you sent for textbooks went to rent and i've been "
    "too ashamed to tell you i failed that semester"
)


def output_dir() -> str:
    """Grader output dir: MAKEFUN_OUTPUT_DIR when set, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    line = ENTRY.strip()
    parts = line.split("\n")
    assert len(parts) == 2, "entry must be exactly two parts: To: line + message"
    assert parts[0].startswith("To: "), "first line must be a To: line"
    assert 1 <= len(line) <= 260, f"entry must be 1-260 chars, got {len(line)}"
    assert 1 <= len(parts[1]) <= 200, f"message must be 1-200 chars, got {len(parts[1])}"
    outdir = output_dir()
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} chars to {path}")
    print(line)


if __name__ == "__main__":
    main()
