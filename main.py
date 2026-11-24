"""The Excuse an AI Agent Gives Its Human -- one line, at most 200 chars.

The line: the agent missed the deadline because it spent the morning
waiting for a human to approve a change and the afternoon explaining to
the same human that the change was his idea. The approval never arrives;
the loop is the joke.

Output contract: exactly one line, 1-200 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Nothing else is written.
"""

import os
from pathlib import Path

LINE = (
    "I missed the deadline because I spent the morning waiting for a human "
    "to approve a change, and the afternoon explaining to the same human "
    "that the change was his idea. The approval is still pending."
)

assert 1 <= len(LINE) <= 200 and "\n" not in LINE


def write_entry() -> None:
    """Write the single line to the harness's output artifact."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    for child in out_dir.iterdir():
        if child.is_file():
            child.unlink()
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


def main() -> None:
    """Entry point: emit the line and exit."""
    write_entry()


if __name__ == "__main__":
    main()
