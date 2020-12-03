#!/usr/bin/env python3

#
# thehungryturnip@gmail.com
#
# Advent of Code 2020: Day 02
#

import re
import sys
from collections import namedtuple

Case = namedtuple('Case', ['min', 'max', 'chr', 'val'])

cases = []
with open('02.in', 'r') as f:
    for l in f.readlines():
        s = re.split('-| |: ', l)
        cases.append(Case(int(s[0]), int(s[1]), s[2], s[3].strip()))

valid_count = 0
for c in cases:
    count = c.val.count(c.chr)
    if count >= c.min and count <= c.max:
        valid_count += 1

print(f'[02a] The number of valid passwords is {valid_count}.')

valid_count = 0
for c in cases:
    if (c.val[c.min - 1] == c.chr) != (c.val[c.max - 1] == c.chr):
        valid_count += 1

print(f'[02b] The number of valid passwords is {valid_count}.')
