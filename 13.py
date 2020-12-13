#!/usr/bin/env python3

from time import perf_counter

def try_to_int(s):
    try:
        return int(s)
    except ValueError:
        return s

def wait_time(time, bus):
    passed = time % bus
    if not passed:
        return 0
    return bus - passed

def find_time(buses):
    time = 100000000000000
    # t = 0
    to_add = 1
    for i, bus in enumerate(buses):
        if bus == 'x':
            continue
        while wait_time(time + i, bus):
            time += to_add
        to_add *= bus
    return time

schedules = []
with open('13.in', 'r') as f:
    time = int(f.readline())
    for s in f.readlines():
        schedules.append([try_to_int(b) for b in s.strip().split(',')])
# print(time)
# print(schedules)

tic = perf_counter()
best_time, best_bus = min([(wait_time(time, b), b) for b in schedules[0] if b != 'x'])
toc = perf_counter()
print(f'[13a] The bus with the least wait time is {best_bus} with a wait time '
      f'of {best_time}: {best_bus * best_time}. ({toc - tic})')

tic = perf_counter()
agreed_time = [find_time(s) for s in schedules]
# print(agreed_time)
toc = perf_counter()
print(f'[13b] The agreable start time is: {agreed_time[0]}. ({toc - tic})')
