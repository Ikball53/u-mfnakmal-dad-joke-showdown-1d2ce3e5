"""Dad Joke Showdown entry: write one dad joke to /output/entry.txt."""

from pathlib import Path

JOKE = (
    "I set the Wi-Fi password to 'incorrect' — so when my kids ask what it is, "
    "I can honestly say: it's incorrect."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
