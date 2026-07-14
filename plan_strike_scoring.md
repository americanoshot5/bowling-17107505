# plan_strike_scoring.md

## Behavior
A strike (first roll of a frame knocks down all 10 pins, frame ends after one roll) adds the next two rolls' pins as a bonus to that frame's score.

## Test
`test_one_strike_adds_next_two_rolls_as_bonus`: roll 10 (strike), then 3, then 4, then 16 more gutter rolls to fill out the remaining frames -> `score() == 24` (frame 1: 10+3+4 bonus = 17, frame 2: 3+4 = 7, rest 0).

## Approach
Extend the frame-by-frame walk in `score()` with a strike check ahead of the spare check:
- If `_rolls[i] == 10` (strike): add `10 + _rolls[i + 1] + _rolls[i + 2]`, advance `i` by **1** (a strike frame consumes only one roll from `_rolls`).
- Else if spare (existing): add `10 + _rolls[i + 2]`, advance `i` by 2.
- Else: add `_rolls[i] + _rolls[i + 1]`, advance `i` by 2.

Add an `_is_strike(i)` helper mirroring `_is_spare(i)`. The 10th frame's extra-roll allowance is still deferred — this increment only adds strike-bonus math to the existing 10-frame loop.
