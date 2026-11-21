"""One-line joke entry for make.fun's "The joke the reviewer laughs at".

Writes a single deterministic joke about working beside an AI coding
agent to /output/entry.txt: UTF-8, no trailing newline, 1-280 code points.
"""

import os

JOKE = "My agent rewrote the whole file, and the only line it kept was the one with the bug."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
