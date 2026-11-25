"""Snooze Button Roast entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt. The line is fixed and deterministic so both grading
runs produce byte-identical output.
"""

import os

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = get_roast()
    validate(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def get_roast() -> str:
    return (
        "My alarm clock rang at 6 AM on a Saturday like it was "
        "the only employee who actually loves Mondays."
    )


def validate(text: str) -> None:
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text:
        raise ValueError("entry must be a single line")


if __name__ == "__main__":
    main()
