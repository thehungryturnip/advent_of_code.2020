#!/usr/bin/env python3

from collections import namedtuple

Instruction = namedtuple('Instruction', ['cmd', 'val'])

class Accumulator(list):
    def add_instruction(self, cmd, val):
        self.append(Instruction(cmd, val))

    def execute_instruction(self, i, a, swap):
        cmd = self[i].cmd
        val = self[i].val

        if cmd == 'nop' or (cmd == 'jmp' and swap):
            return i + 1, a
        if cmd == 'acc':
            return i + 1, a + val
        if cmd == 'jmp' or (cmd == 'nop' and swap):
            return i + val, a

    def execute(self, swap=-1):
        seen = set()
        i = 0
        a = 0
        while i < len(self):
            if i in seen:
                return False, i, a
            seen.add(i)

            i, a = self.execute_instruction(i, a, i==swap)
        return True, i, a

    def attempt_fix(self):
        for i in range(len(self)):
            cmd = self[i].cmd
            if cmd == 'nop' or cmd == 'jmp':
                success, ins, val, = self.execute(i)
                if success:
                    return ins, val

acc = Accumulator()
with open('08.in', 'r') as f:
    for i in f.read().split('\n')[:-1]:
        i = i.split(' ')
        acc.add_instruction(i[0], int(i[1]))

_, ins, val = acc.execute()
print(f'[08a] The loop occured on instruction {ins} with the accumulator '
      f'value of {val}.')

ins, val = acc.attempt_fix()
print(f'[08b] The loop is eliminated by swapping out instruction {ins}. The '
      f'final value is {val}.')
