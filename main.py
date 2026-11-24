"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
Deterministic: no input, no network, no randomness — the same
bytes come out on every run.
"""

import os

JOKE = (
    "My AI therapist listens perfectly, bills by the token, and "
    "still thinks my childhood was a prompt-engineering problem."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise ValueError("entry must be 1 to 280 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
