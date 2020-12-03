#!/usr/bin/env python3

#
# thehungryturnip@gmail.com
#
# Advent of Code 2020: Day 01
#

import sys

TARGET = 2020

with open('01.in', 'r') as f:
    expenses = [int(l) for l in f.readlines()]

looking_for = set()
for e in expenses:
    e_other = TARGET - e
    if e in looking_for:
        print(f'[01a] The 2 entries are {e_other} * {e} = '
              f'{e_other * e}.')
    else:
        looking_for.add(e_other)

for i in range(len(expenses)):
    looking_for = set()
    target = TARGET - expenses[i]
    for j in expenses[i:]:
        e_other = target - j
        if j in looking_for:
            e_i = expenses[i]
            print(f'[01b] The 3 entries are {e_i} * {e_other} * {j} = '
                  f'{e_i * e_other * j}.')
        else:
            looking_for.add(e_other)
