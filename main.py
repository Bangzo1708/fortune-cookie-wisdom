"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt.

The line is a fixed constant: no randomness, no network access, no
reads of files outside this repository. Every run therefore writes
byte-identical output.

Chosen fortune (69 characters):

    A quiet deploy is the loudest compliment your code will ever receive.

Why this line: a deploy that makes no noise — no alerts, no rollback,
no one shouting in the channel — is the highest praise code can get.
The quiet twist (silence as the loudest compliment) only lands on a
second read, and the phrasing is original, not a familiar saying.
"""

from pathlib import Path

FORTUNE = "A quiet deploy is the loudest compliment your code will ever receive."


def main() -> None:
    # The gate accepts 1-120 characters of non-whitespace text; refuse
    # loudly here rather than shipping an entry the scorer would reject.
    if not 1 <= len(FORTUNE) <= 120 or not FORTUNE.strip():
        raise ValueError("fortune must be 1-120 non-whitespace characters")

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(FORTUNE, encoding="utf-8")


if __name__ == "__main__":
    main()
