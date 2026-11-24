"""Dad Joke Showdown entry.

Writes a single deadpan dad joke to /output/entry.txt.
Deterministic, standard library only, no network, no input files.
"""

import os

JOKE = "A stapler is a paperclip that got a promotion and now holds everything together."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The gate refuses entries over 200 characters, so fail loudly here
    # rather than shipping an invalid entry.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
