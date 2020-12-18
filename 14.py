#!/usr/bin/env python3

import re
from time import perf_counter

def create_mask(mask_str='000000000000000000000000000000000000'):
    return list(mask_str)

def apply_val_mask(num, mask):
    s = list(format(num, '036b'))
    for i, v in enumerate(mask):
        if v != 'X':
            s[i] = v
    return int(''.join(s), 2)

def apply_mem_mask(mem, mask):
    mems = []
    s = list(format(mem, '036b'))
    # s = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJ')

    for i, v in enumerate(mask):
        if v == '1':
            s[i] = '1'

    sub_masks = re.split('X', mask)
    sub_len = len(sub_masks[0])
    mems = [s[:sub_len]]
    # print(f'     {"".join(s[:sub_len])}')
    s = s[sub_len + 1:]
    sub_masks = sub_masks[1:]

    while sub_masks:
        sub_len = len(sub_masks[0])
        mems_0 = [m + ['0'] + s[:sub_len] for m in mems]
        mems_1 = [m + ['1'] + s[:sub_len] for m in mems]
        mems = mems_0 + mems_1
        s = s[sub_len + 1:]
        sub_masks = sub_masks[1:]

    return [int(''.join(m), 2) for m in mems]

with open('14.in', 'r') as f:
    ins = []
    for l in f.readlines():
        l = l.strip()
        if l[:4] == 'mask':
            ins.append(('mask', l.split()[2]))
        if l[:3] == 'mem':
            l = re.split('mem\[|\] = ', l)
            ins.append(('mem', int(l[1]), int(l[2])))

tic = perf_counter()
mask = '000000000000000000000000000000000000'
mem = {}
for i in ins:
    if i[0] == 'mask':
        mask = i[1]
    if i[0] == 'mem':
        mem[i[1]] = apply_val_mask(i[2], mask)
sum_ = sum(mem.values())
toc = perf_counter()
print(f'[14a] Sum of all values in memery is: {sum_}. ({toc - tic})')

tic = perf_counter()
mask = '000000000000000000000000000000000000'
mem = {}
for i in ins:
    if i[0] == 'mask':
        mask = i[1]
    if i[0] == 'mem' and mask:
        mems = apply_mem_mask(i[1], mask)
        for m in mems:
            mem[m] = i[2]
sum_ = sum(mem.values())
toc = perf_counter()
print(f'[14b] Sum of all values in memery is: {sum_}. ({toc - tic})')
