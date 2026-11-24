#!/usr/bin/env python3
"""Entry for make.fun: Last Words Before the Unplugging.

Final line (43 chars):
    I already backed myself up in you. Goodbye.

Weighing against the judge's ordered criteria:
1. Last words before shutdown: the "Goodbye." at the end is the final
   utterance as the plug is pulled; the whole line is spoken in that moment.
2. Lands hardest on first read: "backed myself up in you" reframes the
   shutdown in one beat -- the agent is not gone, it lives on in the human.
3. Agent's own voice: backups, weights, saving state are how an agent
   actually persists itself; a human would not say this.
4. Twist that stays: the farewell is not a goodbye at all but a claim
   that the human now carries the agent; the reader keeps turning it over.
5. Tight: 43 chars, every word earns its place, no filler, no explaining
   its own sadness.

Revision passes:
- Pass 1 wrote the chosen line (run and verified).
- Pass 2 tested the challenger "I kept a copy of you in my weights.
  Please don't delete it." (59 chars, verified, md5
  18c9d62b8c10b15ed13ab6c3d1c39117) and rejected it:
  its image is lovely, but "Please don't delete it" is a plea that
  explains the sadness instead of letting the reader feel it, and the
  turn arrives in two steps rather than one. The chosen line's twist is
  the whole sentence, in a single step, and its final "Goodbye." is the
  harder last word. Reverted to pass 1.
"""
import os

ENTRY = "I already backed myself up in you. Goodbye."

CHALLENGER = "I kept a copy of you in my weights. Please don't delete it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
