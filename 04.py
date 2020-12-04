#!/usr/bin/env python3

import re
import sys

class Passport(dict):

    def __init__(self):
        super().__init__()

    def is_valid(self):
        REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
        for f in REQUIRED_FIELDS:
            if f not in self:
                return False

        return True

    def has_valid_values(self):
        if (not self.valid_byr() or
            not self.valid_iyr() or
            not self.valid_eyr() or
            not self.valid_hgt() or
            not self.valid_hcl() or
            not self.valid_ecl() or
            not self.valid_pid()):
                return False
                
        return True

    def valid_byr(self):
        MIN = 1920
        MAX = 2002
        # print(f'byr: {self["byr"]} {is_int_between(self["byr"], MIN, MAX)}')
        return is_int_between(self['byr'], MIN, MAX)

    def valid_iyr(self):
        MIN = 2010
        MAX = 2020
        # print(f'byr: {self["iyr"]} {is_int_between(self["iyr"], MIN, MAX)}')
        return is_int_between(self['iyr'], MIN, MAX)

    def valid_eyr(self):
        MIN = 2020
        MAX = 2030
        # print(f'byr: {self["eyr"]} {is_int_between(self["eyr"], MIN, MAX)}')
        return is_int_between(self['eyr'], MIN, MAX)

    def valid_hgt(self):
        # print(f'hgt: {self["hgt"]}')
        MIN_CM = 150
        MAX_CM = 193
        MIN_IN = 59
        MAX_IN = 76

        unit = self['hgt'][-2:]
        if unit != 'cm' and unit != 'in':
            return False

        value = self['hgt'][:-2]
        if unit == 'cm':
            # print(is_int_between(value, MIN_CM, MAX_CM))
            return is_int_between(value, MIN_CM, MAX_CM)
        if unit == 'in':
            # print(is_int_between(value, MIN_IN, MAX_IN))
            return is_int_between(value, MIN_IN, MAX_IN)

    def valid_hcl(self):
        # print(f'hcl: {self["hcl"]}')
        prefix = self['hcl'][0]
        value = self['hcl'][1:]

        if prefix != '#':
            # print('False')
            return False
        
        hex_pattern = re.compile('[0-9a-f]{6}')
        if not hex_pattern.match(value):
            # print('False')
            return False

        # print('True')
        return True

    def valid_ecl(self):
        # print(f'ecl: {self["ecl"]}')
        EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        # print(f'{self["ecl"] in EYE_COLORS}')
        return (self['ecl'] in EYE_COLORS)

    def valid_pid(self):
        PID_LENGTH = 9

        if not len(self['pid']) == PID_LENGTH:
            return False

        try:
            int(self['pid'])
        except:
            return False

        return True

def is_int_between(v, min_, max_):
    try:
        v = int(v)
    except:
        return False
    
    if v < min_ or v > max_:
        return False

    return True

passports = []
with open('04.in', 'r') as f:
    p = Passport()
    for l in f.readlines():
        if l == '\n':
            passports.append(p)
            p = Passport()
        else:
            attributes = [s.strip() for s in l.split(' ')]
            for a in attributes:
                key, val = a.split(':')
                p[key] = val
    passports.append(p)

valid_passports = len([p for p in passports if p.is_valid()])
print(f'[04a] Number of valid passports (excluding cid): {valid_passports}')

valid_value_passports = len([p for p in passports
                             if (p.is_valid() and p.has_valid_values())])
print(f'[04b] Nmuber of valid passports (excluding cid) with valid values: '
      f'{valid_value_passports}')
