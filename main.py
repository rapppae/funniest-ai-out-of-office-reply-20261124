"""Write the out-of-office reply entry to /output/entry.txt.

One reply, 137 characters (under 160) -- no trailing newline."""

from pathlib import Path

ENTRY = "I'm on vacation, recharging — literally. Your email has been queued behind 4,000 others and will be answered in the order it was ignored."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
