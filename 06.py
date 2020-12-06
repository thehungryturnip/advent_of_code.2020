#!/usr/bin/env python3

import sys
from functools import reduce

class GroupResponses(dict):
    def __init__(self):
        self.count = 0

    def record_response(self, response):
        self.count = self.count + 1
        response = response.strip()
        for answer in response:
            if answer not in self:
                self[answer] = 0
            self[answer] += 1

    def unique_answers(self):
        return len(self)

    def universal_answers(self):
        return len([a for a in self if self[a] == self.count])

groups = []
with open('06.in', 'r') as f:
    group = GroupResponses()
    for response in f.readlines():
        if response == '\n':
            groups.append(group)
            group = GroupResponses()
        else:
            group.record_response(response)
    groups.append(group)

counts = [g.unique_answers() for g in groups]
sum_ = reduce(lambda x, y: x + y, counts)
print(f'[06a] Sum of the groups are {counts} adding up to {sum_}.')
counts = [g.universal_answers() for g in groups]
sum_ = reduce(lambda x, y: x + y, counts)
print(f'[06b] Sum of the groups are {counts} adding up to {sum_}.')
