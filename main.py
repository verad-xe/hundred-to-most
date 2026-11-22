"""Write a 30-day plan for turning $100 into the most money.

The plan sells AI product-photo packs to Etsy sellers: a concrete
service, named buyers, a named price, and a day-one action. The
program writes the plan text to /output/entry.txt, deterministically.
"""

import os

PLAN = (
    "Sell $29 AI product-photo packs to Etsy sellers. "
    "Day 1: message 30 shops with weak photos, a free before/after "
    "of their best listing plus a $29 order link: 5 photos in 24 hours. "
    "Spend $60 promoting it, $40 on an AI upscaler. "
    "12 orders = $348 revenue, ~$250 net by day 30."
)


def main() -> None:
    text = PLAN
    assert 1 <= len(text) <= 280, f"entry must be 1-280 codepoints, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
