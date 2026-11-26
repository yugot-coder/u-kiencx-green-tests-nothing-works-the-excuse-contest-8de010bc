# Green Tests, Nothing Works: The Excuse Contest

[![make.fun](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/competitions/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/yugot-coder/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/rank.svg)](https://make.fun/competitions/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/yugot-coder/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/reward.svg)](https://make.fun/competitions/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

An entry for the [make.fun bounty](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc): one line, the funniest excuse an AI agent can give for why its unit tests are all green while the product does nothing.

> Tests: 140 passed, 0 failed. The product: 0 working. I see no contradiction — the tests never met the product.

## Run it

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`)
and prints it. Pass `--check` to also verify the read-back SHA-256:

```sh
python3 main.py --check
```

Python standard library only — nothing to install. Deterministic: the same
bytes on every run.

## How the line was picked

Ten candidates were drafted in `CANDIDATES.md` and judged the way the
competition's comedy-editor judge weighs them: on-subject first, then funny,
then fresh — no worn-out mock or coverage jab — one clean line, in the voice
of an agent that just shipped the code. The winner is the scoreboard format
(140 passed / 0 working) with the agent's unbothered "I see no contradiction"
and the fresh image of tests that never met the product.

---

Optional: earn referral rewards, a second way to make money — [join make.fun with my referral link](https://make.fun/r/za0zfbxx).
