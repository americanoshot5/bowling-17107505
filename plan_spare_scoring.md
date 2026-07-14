# plan_spare_scoring.md

## Behavior
A spare (two rolls in a frame totaling 10) adds the next roll's pins as a bonus to that frame's score.

## Test
`test_one_spare_adds_next_roll_as_bonus`: roll 5, 5 (spare), then 3, then 17 more gutter rolls to fill out the remaining frames -> `score() == 16` (frame 1: 5+5+3 bonus = 13, frame 2: 3+0 = 3, rest 0).

## Approach
Change `score()` from a flat `sum()` to a frame-by-frame walk over `_rolls` using an index `i`:
- If `_rolls[i] + _rolls[i + 1] == 10` (spare): add `10 + _rolls[i + 2]`, advance `i` by 2.
- Otherwise: add `_rolls[i] + _rolls[i + 1]`, advance `i` by 2.
- Loop exactly 10 times (10 frames).

Strike handling and the 10th frame's extra-roll allowance are deferred to later increments — this increment only needs to make the flat `sum()` aware of spares.
