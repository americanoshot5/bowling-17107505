# plan_gutter_game.md

## Behavior
A game where every roll knocks down 0 pins (a "gutter game") scores 0 total.

## Test
`test_gutter_game_scores_zero`: call `roll(0)` 20 times, then `score()` == 0.

## Approach
`Game` class with:
- `__init__`: store an empty list `_rolls`
- `roll(pins)`: append `pins` to `_rolls`
- `score()`: return `sum(self._rolls)` — correct for this increment since there are no spares/strikes to bonus yet; that logic is deferred to later increments (spare scoring, strike scoring, 10th frame).
