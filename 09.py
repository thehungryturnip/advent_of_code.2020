#!/usr/bin/env python3

def add_two(target, nums):
    looking_for = set()
    for n in nums:
        if n in looking_for:
            return True
        looking_for.add(target - n)
    return False

def sum_to(target, nums):
    j = 2
    sub_sum = sum(nums[0:j])
    for i in range(len(nums)):
        if sub_sum == target:
            return nums[i:j]
        while sub_sum < target:
            sub_sum = sub_sum + nums[j]
            j = j + 1
            if sub_sum == target:
                return nums[i:j]
        sub_sum = sub_sum - nums[i]
    return None

with open('09.in', 'r') as f:
    nums = [int(i) for i in f.readlines()]

PREAMBLE_LENGTH = 25
for i in range(PREAMBLE_LENGTH, len(nums)):
    if not add_two(nums[i], nums[i - PREAMBLE_LENGTH: i]):
        invalid_num = nums[i]
        print(f'[09a] Unable to find 2 numbers that sums to: {invalid_num}.')

contgious_set = sum_to(invalid_num, nums)
min_ = min(contgious_set)
max_ = max(contgious_set)
print(f'[09b] The smallest and largerst numbers in the contgious set that '
      f'sums to {invalid_num} add up to {min_ + max_}.')
