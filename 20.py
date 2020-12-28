#!/usr/bin/env python3

from functools import reduce
from operator import mul

class Tile():
    def __init__(self, s):
        splits = s.strip().split('\n')
        self.id = int(splits[0].split()[1][:-1])
        self.image =[list(r) for r in splits[1:]]
        self.generate_edges()

    def __repr__(self):
        return f'[{self.id}]\n' + '\n'.join([''.join(r) for r in self.image])

    def flip(self):
        self.image = self.image[::-1]

    def rotate(self):
        size = len(self.image) - 1 # assumes that tiles are square
        for r in range(size // 2):
            for c in range(r, size - r):
                top_left = self.image[r][c]
                self.image[r][c] = self.image[size - c][r]
                self.image[size - c][r] = self.image[size - r][size - c]
                self.image[size - r][size - c] = self.image[c][size - r]
                self.image[c][size - r] = top_left

    def generate_edges(self):
        self.edges = set()
        self.edges.add(''.join(self.image[0]))
        self.edges.add(''.join(self.image[-1][::-1]))
        self.rotate()
        self.edges.add(''.join(self.image[0]))
        self.edges.add(''.join(self.image[-1][::-1]))
        self.flip()
        self.edges.add(''.join(self.image[0]))
        self.edges.add(''.join(self.image[-1][::-1]))
        self.rotate()
        self.edges.add(''.join(self.image[0]))
        self.edges.add(''.join(self.image[-1][::-1]))
        self.flip()

    def fits_with(self, other):
        if self is other:
            return 0
        # matches need to // 2 as it will match both directions
        return len([e for e in self.edges if e in other.edges]) // 2

def find_corners_and_edges(tiles):
    corners = set()
    edges = set()
    for t in tiles.values():
        neighbors_count = len(find_neighbors(t, tiles))
        if neighbors_count == 2:
            corners.add(t)
        if neighbors_count == 3:
            edges.add(t)
    return corners, edges

def find_neighbors(to_match, tiles):
    return [t for t in tiles.values() if to_match.fits_with(t)]

tiles = {}
for s in open('20.in').read().split('\n\n'):
    t = Tile(s)
    tiles[t.id] = t

corners, edges = find_corners_and_edges(tiles)
multiple = reduce(mul, [c.id for c in corners])
print(f'[20a] the id multiple of the corners is: {multiple}')
