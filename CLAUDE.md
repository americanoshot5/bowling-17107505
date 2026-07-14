# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project state

`game.py` implements the `Game` class per the task below, built test-first with `pytest` (see `test_game.py`). `main.py` is a small demo script that exercises `Game` with a sample game and prints the score — it is not part of the kata's test suite. See `README.md` for setup/run instructions. There is no lint or CI configuration to defer to.

## Task

Implement the **Bowling Game Kata**: a `Game` class for scoring one game of American ten-pin bowling, built test-first (per the `bowling-tdd` repo name).

Required interface:
- `roll(pins: int) -> None` — called once per ball thrown; `pins` is the number of pins knocked down on that throw.
- `score() -> int` — returns the total score for the complete game.

Scoring rules:
- A game has 10 frames; each frame is normally two rolls (fewer if a strike).
- **Spare** (two rolls knock down all 10 pins): frame score = 10 + pins knocked down on the *next one roll*.
- **Strike** (first roll knocks down all 10 pins, frame ends after one roll): frame score = 10 + pins knocked down on the *next two rolls*.
- **10th frame**: if it's a spare or strike, the player gets extra roll(s) to complete it — up to 3 rolls total in the 10th frame, but no further bonus frames beyond that.

Out of scope per the kata (do not add validation for these):
- Whether a roll/frame is legal (e.g., pin counts that don't add up).
- Whether the right number of rolls/frames have been recorded before `score()` is called.
- Reporting/exposing intermediate per-frame scores — only the final total from `score()` is required.

## Commands

`pytest` is installed in the project `.venv` (Python 3.14). No lint tooling is configured.

- Run all tests: `.venv/Scripts/python.exe -m pytest -q`
- Run a single test: `.venv/Scripts/python.exe -m pytest -q test_game.py::test_one_spare_adds_next_roll_as_bonus`
