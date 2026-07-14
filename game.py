class Game:
    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        total = 0
        i = 0
        for _ in range(10):
            if self._is_strike(i):
                total += 10 + self._rolls[i + 1] + self._rolls[i + 2]
                i += 1
            elif self._is_spare(i):
                total += 10 + self._rolls[i + 2]
                i += 2
            else:
                total += self._rolls[i] + self._rolls[i + 1]
                i += 2
        return total

    def _is_strike(self, i):
        return self._rolls[i] == 10

    def _is_spare(self, i):
        return self._rolls[i] + self._rolls[i + 1] == 10
