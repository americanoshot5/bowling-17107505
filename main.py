from game import Game

FRAMES = [
    (10,),       # frame 1: strike
    (7, 3),      # frame 2: spare
    (9, 0),      # frame 3
    (10,),       # frame 4: strike
    (0, 8),      # frame 5
    (8, 2),      # frame 6: spare
    (0, 6),      # frame 7
    (10,),       # frame 8: strike
    (10,),       # frame 9: strike
    (10, 8, 1),  # frame 10: strike + two bonus rolls
]


def main():
    game = Game()
    for frame in FRAMES:
        for pins in frame:
            game.roll(pins)

    print("Frames:", FRAMES)
    print("Final score:", game.score())


if __name__ == "__main__":
    main()
