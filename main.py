#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip (one line, at most 200 characters)
to /output/entry.txt. Deterministic, no network, no dependencies.
"""

import os

TIP = (
    "Tip: Your agent just deleted the function it called essential, "
    "and every test still passed. Trust the bar. Breathe. "
    "Nobody knows what this code does anymore."
)


def main() -> None:
    assert 1 <= len(TIP) <= 200, "tip must be 1-200 characters"
    assert TIP.strip() == TIP and "\n" not in TIP, "tip must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP + "\n")


if __name__ == "__main__":
    main()
