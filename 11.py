#!/usr/bin/env python3

from functools import lru_cache
from time import perf_counter

class Field(list):
    def __init__(self, description):
        self.description = description.strip()
        self.reset()
        self.los_mode = False

    def __repr__(self):
        return '\n'.join([''.join(r) for r in self])


    def reset(self):
        self.clear()
        for d in self.description.split('\n'):
            self.append(list(d))

    def model(self):
        changes = self.analyze_round()
        while changes:
            self.commit_changes(changes)
            changes = self.analyze_round()

    def analyze_round(self):
        changes = []
        for r in range(len(self)):
            for c in range(len(self[r])):
                v = self[r][c]
                if v == 'L' or v == '#':
                    occupied = self.analyze_seat((r, c))
                    if v == 'L' and occupied == 0:
                        changes.append((r, c, '#'))
                    if v == '#':
                        if ((not self.los_mode and occupied >= 4) or
                            (self.los_mode and occupied >= 5)):
                                changes.append((r, c, 'L'))
        return changes

    def analyze_seat(self, seat):
        directions = (
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1), (0, 1),
                (1, -1), (1, 0), (1, 1),
                )

        return sum([1 for d in directions if self.analyze_los(seat, d)])

    def analyze_los(self, seat, direction):
        r, c = [sum(x) for x in zip(seat, direction)]

        if (r < 0 or r >= len(self) or
            c < 0 or c >= len(self[r])):
                return False

        if self[r][c] == '#':
            return True

        if self[r][c] == 'L':
            return False

        if not self.los_mode:
            return False

        return self.analyze_los((r, c), direction)

    def commit_changes(self, changes):
        for r, c, v in changes:
            self[r][c] = v

    def count_occupied(self):
        return sum([1 for r in self for v in r if v == '#'])

with open('11.in', 'r') as f:
    f = Field(f.read())

tic = perf_counter()
f.model()
occupied = f.count_occupied()
toc = perf_counter()
print(f'[11a] The number of occupied seats is: {occupied}. ({toc - tic}s)')

tic = perf_counter()
f.los_mode = True
f.reset()
f.model()
occupied = f.count_occupied()
toc = perf_counter()
print(f'[11b] The number of occupied seats in line-of-sight mode is: '
      f'{occupied}. ({toc - tic}s)')
