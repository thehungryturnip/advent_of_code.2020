#!/usr/bin/env python3

import sys

class Seat:
    def __init__(self, s):
        BIN_MAP = {
                'F': '0',
                'B': '1',
                'L': '0',
                'R': '1'}
        self.bin_str = ''.join([BIN_MAP[c] for c in s])
    
    def __str__(self):
        return self.str

    def __repr__(self):
        return self.__str__()

    def row(self):
        return int(self.bin_str[:7], 2)

    def col(self):
        return int(self.bin_str[-3:], 2)

    def id(self):
        return int(self.bin_str, 2)

# seats = []
# with open('05.ex', 'r') as f:
    # for l in f.readlines():
        # seats.append(Seat(l.strip()))

# for s in seats:
    # print(s)
    # print(s.row())
    # print(s.col())
    # print(s.id())

seats = []
with open('05.in', 'r') as f:
    for l in f.readlines():
        seats.append(Seat(l.strip()))

max_id = -1
for s in seats:
    if s.id() > max_id:
        max_id = s.id()
        max_seat = s
print(f'[05a] The seat with the max id is at ({max_seat.row()}, '
      f' {max_seat.col()}) with id = {max_seat.id()}).')

taken = set()
possible = set()
for s in seats:
    id_ = s.id()
    taken.add(id_)
    if id_ in possible:
        possible.remove(id_)
    if not (id_ - 1) in taken:
        possible.add(id_ - 1)
    if not (id_ + 1) in taken:
        possible.add(id_ + 1)
# the 1st entry (at index 0) will be from a row that doesn't exist on this
# plane.
open_seat = list(possible)[1]
print(f'[05b] The first open seat has an id of: {open_seat}.')
