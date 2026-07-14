from game import Game


def roll_many(game, n, pins):
    for _ in range(n):
        game.roll(pins)


def test_gutter_game_scores_zero():
    game = Game()
    roll_many(game, 20, 0)

    assert game.score() == 0


def test_all_ones_scores_twenty():
    game = Game()
    roll_many(game, 20, 1)

    assert game.score() == 20


def test_one_spare_adds_next_roll_as_bonus():
    game = Game()
    game.roll(5)
    game.roll(5)
    game.roll(3)
    roll_many(game, 17, 0)

    assert game.score() == 16


def test_one_strike_adds_next_two_rolls_as_bonus():
    game = Game()
    game.roll(10)
    game.roll(3)
    game.roll(4)
    roll_many(game, 16, 0)

    assert game.score() == 24
