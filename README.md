# bowling-tdd

American ten-pin bowling score calculator, built test-first with `pytest`.

## Interface

`Game` (in `game.py`) has two methods:

- `roll(pins: int) -> None` — called once per ball thrown; `pins` is the number of pins knocked down on that throw.
- `score() -> int` — returns the total score for the complete game.

Scoring rules:

- A game has 10 frames; each frame is normally two rolls (fewer if a strike).
- **Spare** (two rolls knock down all 10 pins): frame score = 10 + pins knocked down on the next one roll.
- **Strike** (first roll knocks down all 10 pins, frame ends after one roll): frame score = 10 + pins knocked down on the next two rolls.
- **10th frame**: a spare or strike there earns extra roll(s) to complete the frame — up to 3 rolls total in the 10th frame, with no further bonus frames beyond that.

Out of scope (not validated): whether a roll/frame is legal, whether the right number of rolls has been recorded before `score()` is called, and intermediate per-frame scores.

## Setup

A virtual environment is already set up in `.venv` (Python 3.14). To install dependencies from scratch:

```bash
python -m venv .venv
./.venv/Scripts/pip.exe install pytest
```

## Running the tests

```bash
./.venv/Scripts/python.exe -m pytest -q
```

Run a single test:

```bash
./.venv/Scripts/python.exe -m pytest -q test_game.py::test_one_spare_adds_next_roll_as_bonus
```

## Running the demo

`main.py` rolls a sample 10-frame game (mixing strikes, spares, and open frames) through `Game` and prints the final score:

```bash
./.venv/Scripts/python.exe main.py
```

## Development process

This project was built following the `test-driven-development` skill in `.claude/skills/test-driven-development/`: each behavior gets a `plans/plan_<feature>.md` design note, then a failing test, then the minimal implementation to pass it — with a human-confirmed checkpoint and a commit at each stage. See the git history for the full PLAN → RED → GREEN record.
