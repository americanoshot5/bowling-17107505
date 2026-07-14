# plan_perfect_game.md

## Behavior
A perfect game (12 consecutive strikes: a strike in every one of the 10 frames, plus 2 bonus strikes in the 10th frame) scores 300.

## Test
`test_perfect_game_scores_three_hundred`: call `roll(10)` 12 times, then `score() == 300`.

## Approach
No production code change expected. `score()` already walks exactly 10 frames advancing the index by 1 on every strike, reading `_rolls[i+1]` and `_rolls[i+2]` for the bonus — with 12 rolls in the list this naturally reaches into the two bonus rolls appended after the 10th frame's own strike, without any special-casing for "last frame". This test locks in that the existing strike-scoring logic generalizes correctly to the run of consecutive strikes at the end of the game, including the 10th frame's extra bonus rolls.
