"""Write the make.fun entry: a plan an AI agent can carry out itself to
turn $100 into the most money in 30 days.

The plan text is embedded below as a single deterministic string. Running
this module writes it to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""

import os

PLAN = (
    "Sell $79 Google Profile fixes to US dentists. Day 1: find 200 "
    "dentists on Google Maps with bad profiles and email each a 48-hour "
    "fix offer. Do it free; send proof screenshots. 1 sale per 50 emails "
    "= ~$950 by day 30. Edge: dentists already pay for visibility; every "
    "fix is public."
)


def main() -> None:
    text = PLAN
    assert 1 <= len(text) <= 280, f"entry is {len(text)} codepoints"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
