#!/usr/bin/env python3

import sys

class MapRow(list):
    def __getitem__(self, c):
        return super().__getitem__(c % len(self))

m = []
with open ('03.in', 'r') as f:
    for l in f.readlines():
        m.append(MapRow(l.strip()))

tree_count = 0
for r in range(1, len(m)):
    if m[r][r * 3] == '#':
        tree_count += 1

print(f'[03a] Number of trees along the path is {tree_count}.')
