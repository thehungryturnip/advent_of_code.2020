#!/usr/bin/env python3

import re
from operator import add, mul

def add_multiply(e, add_before_mul):
    SYMBOL_TO_FUNC = {
            '+': add,
            '*': mul,
            }

    if len(e) == 3:
        return SYMBOL_TO_FUNC[e[1]](int(e[0]), int(e[2]))

    if add_before_mul and '+' in e:
        add_at = e.index('+')
        val = add_multiply(e[add_at - 1: add_at + 2], add_before_mul)
        before = e[:add_at - 1]
        after = e[add_at + 2:]
        e = before + [str(val)] + after
        return add_multiply(e, add_before_mul)

    val = add_multiply(e[:3], add_before_mul)
    return add_multiply([str(val)] + e[3:], add_before_mul)

def calc(e, add_before_mul=False):
    pattern = re.compile('\(([^()]+)\)')
    match = pattern.search(e)

    while match:
        val = add_multiply(match[1].split(' '), add_before_mul)
        before = e[:match.start(0)]
        after = e[match.end(0):]
        e = before + str(add_multiply(match[1].split(' '), add_before_mul)) + after
        match = pattern.search(e)

    return add_multiply(e.split(' '), add_before_mul)

with open('18.in', 'r') as f:
    expr = [l.strip() for l in f.readlines()]

# print([calc(e) for e in expr])
total = sum([calc(e) for e in expr])
print(f'[18a] The sum of the expressions is: {total}.')

# print([calc(e, True) for e in expr])
total = sum([calc(e, True) for e in expr])
print(f'[18a] The sum of the expressions is: {total}.')
