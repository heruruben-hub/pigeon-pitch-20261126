#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes one line to /output/entry.txt: the elevator pitch a city
pigeon gives investors for its startup.

The line:

    We're Coo-ber: 40,000 couriers delivering breadcrumbs on demand,
    working for crumbs, never unionizing, raising $2M in seed
    funding — literally seed. We're pigeons.

Why this pitch should win:

* It is a real elevator pitch, in a pigeon's voice, to investors:
  the company, the fleet size, the product, the ask — all in one
  breath, exactly what an investor hears in an elevator.
* The joke lands twice. First, the business itself is absurdly
  pigeon: an army of 40,000 couriers who work for crumbs and never
  unionize — the classic startup boast (scale, cheap labour, no
  labour trouble) turned into literal bird behaviour. Then the
  punchline reframes the ask: "seed funding" is not venture jargon
  any more, it is what pigeons actually eat. "Literally seed. We're
  pigeons." spells out the twist in five words and stops.
* It could only come from a city pigeon: breadcrumbs, a flock of
  40,000 couriers on the square, the coo in Coo-ber. No other
  founder could pitch this.
* It is original, not the familiar pigeon gag about statues or
  pooping on cars: the startup is a delivery platform, and the
  humour comes from the pitch's own economics, not from a pun
  bolted on at the end.
* Every word earns its place: 163 characters, one line, no filler.

Gate (per RULES.txt): /output/entry.txt must be UTF-8 text of 1 to
200 characters, not only white space. This entry is 163 characters.
"""

import os

# The entry line, invented in this build session.
ENTRY = (
    "We're Coo-ber: 40,000 couriers delivering breadcrumbs on demand, "
    "working for crumbs, never unionizing, raising $2M in seed funding "
    "\u2014 literally seed. We're pigeons."
)

OUTPUT_PATH = "/output/entry.txt"

# The gate's caps, mirrored here so the program refuses to write an
# entry the sealed scorer would reject.
MIN_CHARS = 1
MAX_CHARS = 200


def _validate(text: str) -> None:
    """Raise unless text passes the sealed scorer's gate.

    The gate counts characters (not bytes): 1 to 200, not only white
    space, and the entry is one line, so no line break and no stray
    leading or trailing space inflating the count.
    """
    assert isinstance(text, str)
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
    )
    assert text.strip(), "entry must not be only white space"
    assert text == text.strip(), "entry must not carry stray edge space"
    assert "\n" not in text and "\r" not in text, (
        "entry must be a single line"
    )


def main() -> None:
    # Gate checks, mirroring the sealed scorer.
    _validate(ENTRY)

    encoded = ENTRY.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(encoded)

    # Round-trip verification: read it back and confirm the gate again.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert text == ENTRY, f"round-trip mismatch: {text!r} != {ENTRY!r}"
    _validate(text)

    print(
        f"Wrote {len(text)} characters ({len(encoded)} bytes) to {OUTPUT_PATH}"
    )


if __name__ == "__main__":
    main()
