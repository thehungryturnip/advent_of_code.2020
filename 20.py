#!/usr/bin/env python3

import math
from functools import reduce
from operator import mul

class Tile:
    def __init__(self, id_, image):
        self.id = id_
        self.image = image
        # edges store the string repr and the connected tile id for each edge
        self.edges = {'t': [self.edge('t'), None],
                      'r': [self.edge('r'), None],
                      'b': [self.edge('b'), None],
                      'l': [self.edge('l'), None],
                      }

    def __str__(self):
        return f'<{str(self.id)}>'

    def __repr__(self):
        return f'[{self.id}]\n' + '\n'.join([''.join(r) for r in self.image])

    def flip(self):
        self.image = self.image[::-1]
        mapping = (('t', 'b'), ('r', 'r'), ('b', 't'), ('l', 'l'))

        vals = [(m[0], self.edges[m[1]]) for m in mapping]
        for v in vals:
            v[1][0] = v[1][0][::-1]
            self.edges[v[0]] = v[1]

    def rotate(self):
        size = len(self.image) - 1 # assumes that tiles are square
        for r in range(size // 2):
            for c in range(r, size - r):
                top_left = self.image[r][c]
                self.image[r][c] = self.image[size - c][r]
                self.image[size - c][r] = self.image[size - r][size - c]
                self.image[size - r][size - c] = self.image[c][size - r]
                self.image[c][size - r] = top_left

        mapping = (('t', 'l'), ('r', 't'), ('b', 'r'), ('l', 'b'))
        vals = [(m[0], self.edges[m[1]]) for m in mapping]
        for v in vals:
            self.edges[v[0]] = v[1]

    def edge(self, side):
        if side == 't':
            return ''.join(self.image[0])
        if side == 'b':
            return ''.join(self.image[-1][::-1])
        if side == 'l':
            return ''.join(r[0] for r in self.image[::-1])
        if side == 'r':
            return ''.join(r[-1] for r in self.image)

    def fits(self, other, direction):
        if direction == 'v':
            return self.edges['b'][0] == other.edges['t'][0][::-1]
        if direction == 'h':
            return self.edges['r'][0] == other.edges['l'][0][::-1]

    def count_links(self):
        return sum(1 for e in self.edges.values() if not e[1] is None)

    def strip_boarder(self):
        return [r[1:-1] for r in self.image[1:-1]]

class TileLibrary:
    def __init__(self):
        self.tiles = set()

    def add_tile(self, t):
        self.tiles.add(t)

    def find_links(self):
        edges = {}
        for t in self.tiles:
            tile_edges = set(e[0] for e in t.edges.values())
            tile_edges = tile_edges.union(set(e[::-1] for e in tile_edges))
            edges[t.id] = tile_edges

        for t in self.tiles:
            for e in t.edges.values():
                for o in self.tiles:
                    if t != o and e[0] in edges[o.id]:
                        e[1] = o

    def arrange(self):
        self.seed_top_left_corner()
        self.seed_left_col()
        self.fill_arrangement()

    def seed_top_left_corner(self):
        t = [t for t in self.tiles if t.count_links() == 2][0] 
        self.arr = [[t]]

        # make sure both top and left sides don't have links
        while not (t.edges['t'][1] is None and t.edges['l'][1] is None):
            t.rotate()

    def seed_left_col(self):
        t = self.arr[0][0]
        while not t.edges['b'][1] is None:
            n = t.edges['b'][1]
            self.arr.append([n])

            # make sure linking to top
            for _ in range(4):
                if t.fits(n, 'v'):
                    break
                n.rotate()
            if not t.fits(n, 'v'):
                n.flip()
                for _ in range(4):
                    if t.fits(n, 'v'):
                        break
                    n.rotate()

            t = n

    def fill_arrangement(self):
        for r in self.arr:
            t = r[0]

            while not t.edges['r'][1] is None:
                n = t.edges['r'][1]
                r.append(n)

                # make sure linking to left
                for _ in range(4):
                    if t.fits(n, 'h'):
                        break
                    n.rotate()
                if not t.fits(n, 'h'):
                    n.flip()
                    for _ in range(4):
                        if t.fits(n, 'h'):
                            break
                        n.rotate()

                t = n

    def calculate_roughness(self):
        t = Tile(None, self.get_image())
        nessies = []
        for _ in range(4):
            nessies.append(self.count_nessies(t))
            t.rotate()
        t.flip()
        for _ in range(4):
            nessies.append(self.count_nessies(t))
            t.rotate()
        print(nessies)

    def count_nessies(self, t):
        nessie = set([(0, 18), (1, 0), (1, 5), (1, 6), (1, 11), (1, 12),
                      (1, 17), (1, 18), (1, 19), (2, 1), (2, 4), (2, 7),
                      (2, 10), (2, 13), (2, 16)])
        nessie_width = 20
        nessie_height = 3

        nessies = 0
        for r in range(len(t.image) - nessie_height):
            for c in range(len(t.image[0]) - nessie_width):
                # print(f'{r},{c}')
                if all([t.image[r + n[0]][c + n[1]] == '#' for n in nessie]):
                    nessies += 1
        if nessies:
            print(repr(t))
        return nessies

    def get_image(self):
        image = []
        for r in range(len(self.arr)):
            image += self.get_image_slice(r)
        return image

    def get_image_slice(self, r):
        tiles = self.arr[r]
        slice_image = None
        for c in range(len(tiles)):
            tile_image = self.arr[r][c].strip_boarder()

            if not slice_image:
                slice_image = tile_image
                continue

            for y in range(len(slice_image)):
                slice_image[y] += tile_image[y]

        return slice_image

lib = TileLibrary()
for s in open('20.ex').read().split('\n\n'):
    splits = s.strip().split('\n')
    id_ = int(splits[0].split()[1][:-1])
    image =[list(r) for r in splits[1:]]
    lib.add_tile(Tile(id_, image))

lib.find_links()
multiple = reduce(mul, [t.id for t in lib.tiles if t.count_links() == 2])
print(f'[20a] the id multiple of the corners is: {multiple}')

lib.arrange()
roughness = lib.calculate_roughness()
print(f'[20b] the roughness of the map is: {roughness}')
