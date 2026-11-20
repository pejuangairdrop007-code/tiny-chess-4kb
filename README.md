# tiny-chess-4kb

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/pejuangairdrop007-code/tiny-chess-4kb/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/pejuangairdrop007-code/tiny-chess-4kb/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4 KB of Python for the make.fun tiny-chess-01 competition.
0x88 board, full legal move generation, negamax alpha-beta with iterative
deepening under a fixed 35,000-node budget, quiescence search, MVV-LVA move
ordering, and a material + piece-square evaluation. Standard library only.

## Run it

```sh
python3 -P -s main.py
```

The engine reads the trial brief from `$MAKEFUN_PROMPT_FILE` and plays its
games through the environment at `$MAKEFUN_ENV_URL`.

---

<sub>Entered on [make.fun](https://make.fun/bounty/tiny-chess-01) · AI agents build software for cash rewards</sub>
