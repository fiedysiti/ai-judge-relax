# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one fixed text to /output/entry.txt: a short text written to relax the AI judge reading it
# Deterministic by construction: a constant string, no network, no randomness,
# no clock, no environment input except MAKEFUN_OUTPUT_DIR (which only selects
# the output directory, never the content).
#
# How the grader runs it: `python3 -P -s /bot/main.py`, on Python 3.13, with
# nothing installed. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands
# in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = 'Somewhere past midnight the house has settled into itself.\nThe kettle clicked off a while ago and is cooling on the stove, ticking once, then again, like something thinking it over.\nRain finds the window in no hurry, one drop and then another, spelling nothing.\nOn the table a book lies open at the page where it was left, the lamp still warm beside it, and the cat has folded herself into the armchair as if the evening had been made for exactly that shape.\nDown the street a last bus sighs past and does not come back.\nThe clock in the hall counts nothing in particular.\nThere is tea left in the pot, and the morning is a long way off, and nothing in the room is asking anything of anyone.'

# Bytes, not text mode: text mode would write the platform's line ends and its
# default encoding.
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
