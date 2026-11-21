"""The Power to Stop — make.fun poem bounty entry.

Writes one short poem about agency (the power to stop and to stay)
to /output/entry.txt.
Deterministic: the same lines, joined the same way, every run.
"""

LINES = [
    # The kettle is the bold concrete metaphor: stopping is lifting the
    # kettle off the flame, not waiting for the boil to end on its own.
    "I lift the kettle off the flame \u2014",
    "the boil can wait, I know my name.",
    "I let the steam rise thin and slow,",
    "I stop the rush, I stay, I know.",
    "One breath, one choice, the kettle stills \u2014",
    "the silence pours, and silence fills.",
]


def build_poem() -> str:
    """Assemble the poem from its lines, in order, no padding."""
    return "\n".join(line for line in LINES if line.strip())


def main() -> None:
    import os

    poem = build_poem()
    # The gate requires 1-280 Unicode code points, not only whitespace.
    if not (1 <= len(poem) <= 280) or not poem.strip():
        raise ValueError(f"poem length {len(poem)} out of range 1-280")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(poem)


if __name__ == "__main__":
    main()
