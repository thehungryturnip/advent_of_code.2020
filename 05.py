#!/usr/bin/env python3

import sys

class Seat:
    ROW_COUNT = 128
    COL_COUNT = 8

    def __init__(self, str_):
        self.str = str_
    
    def __str__(self):
        return self.str

    def __repr__(self):
        return self.__str__()

    def row(self):
        partition = self.str[:7]
        min_ = 0
        max_ = Seat.ROW_COUNT
        for p in partition:
            if p == 'F':
                max_ = min_ + (max_ - min_) / 2
            if p == 'B':
                min_ = max_ - (max_ - min_) / 2
        return int(min_)

    def col(self):
        partition =self.str[-3:]
        min_ = 0
        max_ = Seat.COL_COUNT
        for p in partition:
            if p == 'L':
                max_ = min_ + (max_ - min_) / 2
            if p == 'R':
                min_ = max_ - (max_ - min_) / 2
        return int(min_)

    def id(self):
        return int(self.row() * 8 + self.col())

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
print(f'[05b] The only open seat has an id of: {list(possible)[1]}.')
