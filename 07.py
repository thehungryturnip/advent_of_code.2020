#!/usr/bin/env python3

bags = dict()
with open('07.in', 'r') as f:
    for desc in f.readlines():
        desc = desc.strip().split(' ')
        name = ' '.join(desc[:2])
        bag = dict()
        i = 4
        while i < len(desc):
            if desc[i] == 'no':
                break
            count = int(desc[i])
            inside = ' '.join(desc[i + 1: i + 3])
            bag[inside] = count
            i += 4
        bags[name] = bag

def bag_contains(bag, target):
    if target in bag:
        return True
    return any([bag_contains(bags[b], target) for b in bag])

valid_bags = []
for b in bags:
    # print(b)
    if bag_contains(bags[b], 'shiny gold'):
        # print('True')
        valid_bags.append(b)
count = len(valid_bags)
print(f'[07a] The number of outer bags that contain \'shiny gold\' is: '
      f'{count}.')

def bag_count(bag):
    return 1 + sum([bag_count(bags[b]) * bag[b] for b in bag])

count = bag_count(bags['shiny gold']) - 1
print(f'[07b] The number of bags inside required to carry a shiny gold bag '
      f'is: {count}.')
