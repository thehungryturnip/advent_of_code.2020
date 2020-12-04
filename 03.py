#!/usr/bin/env python3

import sys
from collections import namedtuple
from functools import reduce

Slope = namedtuple('Slope', ['dr', 'dc'])

class MapRow(list):
    def __getitem__(self, c):
        return super().__getitem__(c % len(self))

def count_trees(m, s):
    tree_count = r = c = 0
    while r < len(m):
        if m[r][c] == '#':
            tree_count += 1
        r += s.dr
        c += s.dc
    return tree_count

m = []
with open('03.in', 'r') as f:
    for l in f.readlines():
        m.append(MapRow(l.strip()))

trees = count_trees(m, Slope(1, 3))
print(f'[03a] Number of trees along the path is {trees}.')

slopes = [Slope(1, 1), Slope(1, 3), Slope(1, 5), Slope(1, 7), Slope(2, 1)]
trees = list(map(lambda s: count_trees(m, s), slopes))
multiply = reduce(lambda t1, t2: t1 * t2, trees)
print(f'[03b] The tree counts for slopes {slopes} are {trees} which multiply to {multiply}.')
