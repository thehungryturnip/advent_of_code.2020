#!/usr/bin/env python3

from copy import deepcopy
from time import perf_counter

rounds = 1
starter = {}
with open('15.in', 'r') as f:
    for num in [int(num) for num in f.readline().strip().split(',')]:
        starter[num] = [rounds]
        prev = num
        rounds += 1
starter_prev = prev
starter_rounds = rounds

tic = perf_counter()
spoken = deepcopy(starter)
prev = starter_prev
rounds = starter_rounds
while rounds <= 2020:
    if not prev in spoken or len(spoken[prev]) == 1:
        num = 0
    else:
        num = spoken[prev][-1] - spoken[prev][-2]
    
    if not num in spoken:
        spoken[num] = []

    spoken[num].append(rounds)
    prev = num
    rounds += 1
toc = perf_counter()
print(f'[15a] The final number after 2020 rounds is: {num}. ({toc - tic})')

tic = perf_counter()
spoken = deepcopy(starter)
prev = starter_prev
rounds = starter_rounds
while rounds <= 30000000:
    if not prev in spoken or len(spoken[prev]) == 1:
        num = 0
    else:
        num = spoken[prev][-1] - spoken[prev][-2]
    
    if not num in spoken:
        spoken[num] = []

    spoken[num].append(rounds)
    prev = num
    rounds += 1
toc = perf_counter()
print(f'[15b] The final number after 30000000 rounds is: {num}. ({toc - tic})')
