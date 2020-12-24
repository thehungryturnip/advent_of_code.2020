#!/usr/bin/env python3

import regex as re

def expand_rule(r):
    if not r.isnumeric():
        return r
    return '(?:' + ''.join(map(expand_rule, rules[r].split())) + ')'

with open('19.in', 'r') as f:
    rules_txt, messages_txt = f.read().split('\n\n', 1)

rules = dict(
        rule_txt.replace('"', '').split(': ', 1)
        for rule_txt in rules_txt.splitlines()
        )
messages = messages_txt.splitlines()

pattern = re.compile(expand_rule('0'))
valid_count = sum(pattern.fullmatch(m) is not None for m in messages)
print(f'[19a] The number of messages matching rule 0 is: {valid_count}')

# rules['8'] = '42 | 42 8'
rules['8'] = '42 +'
# rules['11'] = '42 31 | 42 11 31'
rules['11'] = '(?P<repeat> 42 (?&repeat)? 31 )'
pattern = re.compile(expand_rule('0'))
valid_count = sum(pattern.fullmatch(m) is not None for m in messages)
print(f'[19b] The number of messages matching rule 0 is: {valid_count}')
