#!/usr/bin/env python3

import time

def count_gaps(jolts):
    gaps = dict()
    for i, a in enumerate(jolts):
        g = a
        if i != 0:
            g = g - jolts[i - 1]
        if not g in gaps:
            gaps[g] = 0
        gaps[g] = gaps[g] + 1
    return gaps

def count_options(jolts):

    cache = {
            0:1,
            }

    def count_suboptions(jolts):
        target = jolts[-1]
        if target in cache:
            return cache[target]

        def candidates_generator(jolts):
            i = len(jolts) - 2
            while i >= 0 and jolts[-1] - jolts[i] <= 3:
                yield i
                i = i - 1

        candidates = [i for i in candidates_generator(jolts)]
        options = sum([count_suboptions(jolts[:c + 1]) for c in candidates])

        cache[target] = options
        return options

    return count_suboptions(jolts)

jolts = []
# with open('10.ex', 'r') as f:
# with open('10.ex2', 'r') as f:
with open('10.in', 'r') as f:
    for a in f.readlines():
        jolts.append(int(a))
jolts.append(0) # adding the outlet
jolts.append(max(jolts) + 3) # adding the device
jolts.sort()

tic = time.perf_counter_ns()
gaps = count_gaps(jolts)
toc = time.perf_counter_ns()
print(f'[10a] The number of 1-jolt and 3-jolt gaps are {gaps[1]} and '
      f'{gaps[3]}, which mulitply to {gaps[1] * gaps[3]}. ({toc - tic}ns)')

tic = time.perf_counter_ns()
options_count = count_options(jolts)
toc = time.perf_counter_ns()
print(f'[10b] The number of options is: {options_count}. ({toc - tic}ns)')
