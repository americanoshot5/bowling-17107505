# plan_all_ones.md

## Behavior
A game where every roll knocks down 1 pin (no strikes or spares) scores 20 total.

## Test
`test_all_ones_scores_twenty`: call `roll(1)` 20 times, then `score()` == 20.

## Approach
No production code change expected. The current `score()` (`sum(self._rolls)`) already sums plain rolls correctly when there are no spares/strikes to bonus — this test locks that behavior in as a regression guard before spare/strike scoring is added next, which will require changing `score()` away from a flat sum.
