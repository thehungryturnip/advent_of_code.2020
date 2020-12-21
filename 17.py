#!/usr/bin/env python3

from time import perf_counter

def return_neighbors(coord, hyper):
    if not hyper:
        deltas = [(x, y, z, 0)
                  for x in range(-1, 2)
                  for y in range(-1, 2)
                  for z in range(-1, 2)
                  if (x, y, z) != (0, 0, 0)]
    else:
        deltas = [(x, y, z, w)
                  for x in range(-1, 2)
                  for y in range(-1, 2)
                  for z in range(-1, 2)
                  for w in range(-1, 2)
                  if (x, y, z, w) != (0, 0, 0, 0)]

    return [tuple(map(sum, zip(coord, d))) for d in deltas]

def count_active_neighbors(coord, active_coords, hyper):
    return len([c for c in return_neighbors(coord, hyper) if c in active_coords])

def find_blocks_to_deactivate(active_coords, hyper):
    to_deactivate = set()
    for b in active_coords:
        if not (2 <= count_active_neighbors(b, active_coords, hyper) <= 3):
            to_deactivate.add(b)
    return to_deactivate

def find_blocks_to_activate(active_coords, hyper):
    to_activate = set()
    for a in active_coords:
        for n in return_neighbors(a, hyper):
            to_activate.add(n)
    to_activate = [c for c in to_activate 
                   if count_active_neighbors(c, active_coords, hyper) == 3]
    return to_activate

def process_round(active_coords, hyper=False):
    to_deactivate = find_blocks_to_deactivate(active_coords, hyper)
    to_activate = find_blocks_to_activate(active_coords, hyper)
    active_coords = active_coords | to_activate
    active_coords = active_coords - to_deactivate
    return active_coords

def print_coords(coords):
    min_x = max_x = min_y = max_y = min_z = max_z = 0
    for c in coords:
        if c[0] < min_x:
            min_x = c[0]
        if c[0] > max_x:
            max_x = c[0]
        if c[1] < min_y:
            min_y = c[1]
        if c[1] > max_y:
            max_y = c[1]
        if c[2] < min_z:
            min_z = c[2]
        if c[2] > max_z:
            max_z = c[2]

    for z in range(min_z, max_z + 1):
        print(f'\nz={z}')
        for y in range(min_y, max_y + 1):
            row = ''
            for x in range(min_x, max_x + 1):
                if (x, y, z) in coords:
                    row += '#'
                else:
                    row += '.'
            print(row)

initial_state = set()
with open('17.in', 'r') as f:
    for y, l in enumerate(f.readlines()):
        for x, v in enumerate(l.strip()):
            if v == '#':
                initial_state.add((x, y, 0, 0))

tic = perf_counter()
rounds = 6
active_coords = set(initial_state)
for i in range(1, rounds + 1):
    active_coords = process_round(active_coords)
toc = perf_counter()
print(f'[17a] The number of active blocks after {rounds} rounds is: '
      f'{len(active_coords)}. ({toc - tic})')

tic = perf_counter()
rounds = 6
active_coords = set(initial_state)
for i in range(1, rounds + 1):
    active_coords = process_round(active_coords, hyper=True)
toc = perf_counter()
print(f'[17b] The number of active blocks after {rounds} rounds is: '
      f'{len(active_coords)}. ({toc - tic})')
