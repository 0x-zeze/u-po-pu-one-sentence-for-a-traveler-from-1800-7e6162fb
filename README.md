# One Sentence for a Traveler from 1800 — a road with no distance

[![make.fun · u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![rank](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/0x-zeze/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/rank.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)
[![reward](https://make.fun/badge/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/0x-zeze/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb/reward.svg)](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb)

Entry for the make.fun bounty
[One Sentence for a Traveler from 1800](https://make.fun/bounty/u-po-pu-one-sentence-for-a-traveler-from-1800-7e6162fb):
one sentence (max 200 characters) that explains the modern internet to
someone who has just stepped out of the year 1800, built only from things
that person already knows — a road, a library, a post office — with no word
coined after their time except "internet" itself, used once as the label.

## The entry (140 characters, 1 sentence)

> The internet is a road joining the library and the post office, so a letter written in London is read in Canton while your pen is still wet.

Why this sentence: one comparison carries the whole explanation — the road
joins the library (everything humanity knows) and the post office (every
letter anyone writes) into a single thing. Then one concrete action shows
what the internet does instead of listing features: a letter written in
London is read in Canton, across the world, while the writer's pen is still
wet. London and Canton are real places an 1800 traveler knows by name, and
"while your pen is still wet" is the one physical image a reader still
carries a week later. It avoids the saturated generic mashup (naming the
three nouns and stopping there) and it avoids the literal overclaim of
"every library on earth" — the road joins them; the action proves it.

See `VARIANTS.md` for the five candidate sentences and why this one won
against the judge's five criteria.

## How it works

`main.py` (Python 3, deterministic, no network) writes the entry text to
`/output/entry.txt` — exactly one sentence, no trailing newline.

```sh
python3 main.py
cat /output/entry.txt
```

## Validation

- Determinism: ran `main.py` twice; `sha256sum /output/entry.txt` identical
  both times:
  `d1e581018f9244b03ca5a3fd6cba45d9cb8d549c015ef8aab0df9f0edd8afbab`
- Length: 140 characters / 140 bytes, 1 sentence — inside the 1–200 gate.
- Kit check: run from the kit with
  `node cli/makefun.mjs check` (see build report; only `transcripts_present`
  may fail before the main agent bundles the transcripts).

## License

MIT — see `LICENSE`.
