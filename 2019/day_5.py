#!/usr/bin/env python3

import json
from operator import add, mul
import sys

# Read opecode (if := 99 then exit)
# Add position prefix (s = '0' * (5-len(s)) + s)
# Parse position modes and set operands
# If write mode - write, ptr += 2
# If read mode - read, ptr += 2

def parse_opcode_and_modes(operator):
    operator = '0' * (5-len(operator)) + operator
    opcode = operator[3:]
    modes = operator[:3]
    return opcode, modes

def get_operand(opcodes, ptr, mode):
    print(f'DEBUG {opcodes} {ptr:<10} {mode:<10}')
    if int(mode) == 0:
        rv = int(opcodes[int(opcodes[ptr])])
    else:
        rv = int(opcodes[ptr])
    print(f'\t Operand: {rv}, mode: {mode}, ptr: {ptr}')
    return rv

def get_operands(opcodes, ptr, modes, count):
    rv = []
    for i in range(count):
        rv.append(get_operand(opcodes, ptr+i, modes[i]))
    return rv

def run(opcodes, stdin=sys.stdin, stdout=sys.stdout):
    ptr = 0
    while (operator := intcodes[ptr]) != '99' and (ptr < len(intcodes)):
        opcode, modes = parse_opcode_and_modes(operator)
        print(opcode, modes)
        # Zero-pad to length 5
        if opcode in ('02', '03'):
            op = mul if opcode == '02' else add
            operands = get_operands(opcodes, ptr+1, modes, 2)
            destination_ptr = int(opcodes[ptr+3])
            print(f'Operands: {operands}, destination_ptr: {destination_ptr}')
            opcodes[destination_ptr] = op(*operands)
            print(opcodes)
        break

if __name__ == '__main__':
    with open('day_5.txt') as f:
        intcodes = f.read().split(',')
        intcodes = ['1002', '4', '3', '4', '33']
        run(intcodes)
