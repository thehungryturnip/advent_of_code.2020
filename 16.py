#!/usr/bin/env python3

import re
from collections import defaultdict
from functools import reduce
from time import perf_counter

def is_valid_val(val, fields):
    return any([range_[0] <= val <= range_[1] 
                for field in fields 
                for range_ in fields[field]])

def find_invalid_vals(ticket, fields):
    return [val for val in ticket if not is_valid_val(val, fields)]

def sum_invalid_vals(ticket, fields):
    return sum(find_invalid_vals(ticket, fields))

def val_in_ranges(val, ranges):
    for r in ranges:
        if r[0] <= val <= r[1]:
            return True
    return False
    return any([range_[0] <= val <= range_[1] for range_ in ranges])

def vals_in_ranges(vals, ranges):
    for v in vals:
        if not val_in_ranges(v, ranges):
            return False
    return True
    return all([val_in_ranges(val, ranges) for val in vals])

def potential_fields(vals, fields):
    potential = []
    for f in fields:
        if vals_in_ranges(vals, fields[f]):
            potential.append(f)
    return potential
    return [f for f in fields if vals_in_ranges(vals, fields[f])]

def clear_position(position, candidates):
    for positions in candidates.values():
        if position in positions:
            positions.remove(position)

def analyze_positions(nearby, fields):
    candidates = defaultdict(set)
    for position in range(len(nearby[0])):
        vals = [n[position] for n in nearby]
        possible = potential_fields(vals, fields)
        for f in possible:
            candidates[f].add(position)

    confirmed = {}
    while len(confirmed) < len(fields):
        for field in candidates:
            positions = candidates[field]
            if len(positions) == 1:
                position = next(iter(positions))
                clear_position(position, candidates)
                confirmed[field] = position

    return confirmed

with open('16.in', 'r') as f:
    fields = {}
    l = f.readline()
    while l != '\n':
        s = re.split(': |-| or ', l.strip())
        fields[s[0]] = ((int(s[1]), int(s[2])), (int(s[3]), int(s[4])))
        l = f.readline()
    
    # skip blank row and "your ticket"
    for i in range(2):
        l = f.readline()
    mine = [int(n) for n in l.strip().split(',')]

    # skip blank row and "nearby tickets"
    for i in range(2):
        l = f.readline()
    nearby = []
    for l in f.readlines():
        nearby.append([int(n) for n in l.strip().split(',')])

tic = perf_counter()
invalid_sum = sum([sum_invalid_vals(t, fields) for t in nearby])
toc = perf_counter()
print(f'[16a] Error rate is: {invalid_sum}. ({toc - tic})')

tic = perf_counter()
nearby = [t for t in nearby if len(find_invalid_vals(t, fields)) == 0]
positions = analyze_positions(nearby, fields)
multiple = reduce(lambda x, y: x * y, 
                  [mine[positions[p]] for p in positions
                   if p[:10] == 'departure '])
toc = perf_counter()
print(f'[16b] Multiple of departure fields is: {multiple}. ({toc - tic})')
