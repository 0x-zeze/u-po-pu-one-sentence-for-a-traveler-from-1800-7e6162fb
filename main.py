#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800 — one sentence, no network, deterministic."""
import os

ENTRY = "The internet is a road joining the library and the post office, so a letter written in London is read in Canton while your pen is still wet."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
