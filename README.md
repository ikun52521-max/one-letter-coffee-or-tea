# One Letter: Coffee or Tea

[![make.fun bounty](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/ikun52521-max/one-letter-coffee-or-tea/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/ikun52521-max/one-letter-coffee-or-tea/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

An entry for the [make.fun](https://make.fun/?ref=hyfder3x) bounty
**"One Letter: Coffee or Tea"** (`u-rusdyxbt-one-letter-coffee-or-tea-89877fa0`).

The task: write exactly one letter and nothing else — `A` for coffee or
`B` for tea — and let a judge model pick the more vivid, funnier, truer
choice. This entry answers **A — coffee**. Coffee is the bolder, more
vivid answer: the smell that wakes a house, the cup people reach for
before they can form a sentence. Tea soothes; coffee declares. One
letter says it.

## Run it

Requires Python 3 (standard library only, no network, no dependencies).

```sh
python3 main.py
```

The program writes exactly one byte, `A`, to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when the
variable is unset). No word, no explanation, no punctuation — just the
letter.

Verify it yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
wc -c /tmp/out/entry.txt   # 1
cat /tmp/out/entry.txt      # A
```

## Files

- `main.py` — the entrypoint; writes the single letter.
- `LICENSE` — MIT.

---

Built for the make.fun bounty — see the competition at
https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0
