# plan_tenth_frame_spare.md

## Behavior
A spare in the 10th (final) frame gets exactly one bonus roll counted, and the game ends after that — no frame 11 is scored.

## Test
`test_spare_in_tenth_frame_gets_one_bonus_roll`: 9 frames of gutters (18 rolls of 0), then in the 10th frame roll 5, 5 (spare), then one bonus roll of 4 -> `score() == 14` (frames 1-9: 0, frame 10: 5+5+4 = 14).

## Approach
No production code change expected. `score()`'s loop runs exactly `range(10)` frames; when it reaches the 10th frame it applies the existing `_is_spare` branch (`10 + _rolls[i + 2]`) exactly as it would for any other frame, then the loop ends — the bonus roll is read from `_rolls` but no 11th frame is ever scored. This test locks in that the spare-scoring logic generalizes to the frame-10-specific case (a spare that is not followed by more full frames), distinct from the earlier `test_one_spare_adds_next_roll_as_bonus` which used the spare in frame 1.
