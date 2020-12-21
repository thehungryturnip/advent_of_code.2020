#!/usr/bin/env python3

import re
from operator import add, mul

def add_mul(e, add_then_mul):
    SYMBOL_TO_FUNC = {
            '+': add,
            '*': mul,
            }

    if len(e) == 3:
        return SYMBOL_TO_FUNC[e[1]](int(e[0]), int(e[2]))

    if add_then_mul and '+' in e:
        add_at = e.index('+')
        val = add_mul(e[add_at - 1: add_at + 2], add_then_mul)
        before = e[:add_at - 1]
        after = e[add_at + 2:]
        e = before + [str(val)] + after
        return add_mul(e, add_then_mul)

    val = add_mul(e[:3], add_then_mul)
    return add_mul([str(val)] + e[3:], add_then_mul)

def calc(e, add_then_mul=False):
    pattern = re.compile('\(([^()]+)\)')
    match = pattern.search(e)

    while match:
        val = add_mul(match[1].split(' '), add_then_mul)
        before = e[:match.start(0)]
        after = e[match.end(0):]
        e = before + str(add_mul(match[1].split(' '), add_then_mul)) + after
        match = pattern.search(e)

    return add_mul(e.split(' '), add_then_mul)

with open('18.in', 'r') as f:
    expr = [l.strip() for l in f.readlines()]

# print([calc(e) for e in expr])
total = sum([calc(e) for e in expr])
print(f'[18a] The sum of the expressions is: {total}.')

# print([calc(e, True) for e in expr])
total = sum([calc(e, True) for e in expr])
print(f'[18a] The sum of the expressions is: {total}.')
