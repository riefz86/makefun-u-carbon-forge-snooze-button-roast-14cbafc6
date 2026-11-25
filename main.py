"""Snooze Button Roast.

Writes one roast line to /output/entry.txt: an alarm clock that rings
at 6 AM on a Saturday morning.
"""

import os

LINE = "My alarm clock went off at 6 AM on a Saturday like it had a court date and I was its alibi."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
