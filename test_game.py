from game import Game


def roll_many(game, n, pins):
    for _ in range(n):
        game.roll(pins)


def test_gutter_game_scores_zero():
    game = Game()
    roll_many(game, 20, 0)

    assert game.score() == 0
