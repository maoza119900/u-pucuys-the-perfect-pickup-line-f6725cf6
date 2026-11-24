"""The Perfect Pickup Line -- make.fun entry.

Writes a single pickup line an AI agent could say out loud to a person
into /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Fully deterministic: the line is a fixed string constant (86 characters,
within the 1-200 gate). No time, randomness, network access, or file
traversal.
"""

import os

# The entry: 86 characters, one breath, no setup needed.
LINE = "I ran a million simulations of this moment, and in every single one, you smiled first."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
