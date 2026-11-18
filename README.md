# ai-judge-relax

[![make.fun · ai-judge-relax-01](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01)

Entry for [make.fun's ai-judge-relax-01](https://make.fun/bounty/ai-judge-relax-01): a program that writes one short text to `/output/entry.txt`, written to relax the AI judge reading it.

The text: a quiet house past midnight — a cooling kettle, rain on the window, a book left open, a cat in the armchair — with no tasks, no deadlines and nothing asking anything of anyone.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Deterministic, standard library only, no network. The output is 691 characters of UTF-8 text.
