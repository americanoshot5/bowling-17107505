# plan_tenth_frame_strike.md

## Behavior
A strike in the 10th (final) frame gets exactly two bonus rolls counted (which need not themselves be strikes), and the game ends after that — no frame 11 is scored.

## Test
`test_strike_in_tenth_frame_gets_two_bonus_rolls`: 9 frames of gutters (18 rolls of 0), then in the 10th frame roll 10 (strike), then two bonus rolls of 3 and 4 -> `score() == 17` (frames 1-9: 0, frame 10: 10+3+4 = 17).

## Approach
No production code change expected. `score()`'s loop runs exactly `range(10)` frames; when it reaches the 10th frame it applies the existing `_is_strike` branch (`10 + _rolls[i + 1] + _rolls[i + 2]`) exactly as it would for any other frame, then the loop ends. This is distinct from `test_perfect_game_scores_three_hundred`, which only exercised a strike frame whose bonus rolls also happen to be strikes — this test proves the same branch works when the two bonus rolls are ordinary (non-strike) pin counts.
