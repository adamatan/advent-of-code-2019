#!/usr/bin/env python3

import json
from operator import add, mul
import sys
import logging

logger = logging.getLogger('root')
FORMAT = "[%(funcName)30s() ]   %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


# logging.basicConfig(level=logging.DEBUG)
# Read opecode (if := 99 then exit)
# Add position prefix (s = '0' * (5-len(s)) + s)
# Parse position modes and set operands
# If write mode - write, ptr += 2
# If read mode - read, ptr += 2

def parse_opcode_and_modes(operator):
    padded_operator = str(operator)
    padded_operator = '0' * (5-len(padded_operator)) + padded_operator
    opcode = int(padded_operator[3:])
    modes = [int(i) for i in padded_operator[:3]]
    logger.debug(f'Operator: {operator:<5}'
                 f'Padded operator: {padded_operator:<10}'
                 f'Opcode: {opcode:<5}'
                 f'Modes: {str(modes):<10}')
    return opcode, modes

def get_operand(opcodes, ptr, mode):
    if int(mode) == 0:
        rv = int(opcodes[int(opcodes[ptr])])
    else:
        rv = int(opcodes[ptr])
    logger.debug(f'Operand: {rv}, mode: {mode}, ptr: {ptr}')
    return rv

def get_operands(opcodes, ptr, modes, count):
    rv = []
    for i in range(count):
        rv.append(get_operand(opcodes, ptr+i, modes[i]))
    return rv

def run(opcodes, stdin=sys.stdin, stdout=sys.stdout):
    ptr = 0
    while (operator := intcodes[ptr]) != 99 and (ptr < len(intcodes)):
        logger.debug(f'ptr: {ptr}, opcodes[ptr]: {opcodes[ptr]}')
        opcode, modes = parse_opcode_and_modes(operator)
        if opcode in (1, 2):
            op = mul if opcode == 2 else add
            operands = get_operands(opcodes, ptr+1, modes, 2)
            destination_ptr = int(opcodes[ptr+3])
            logger.debug(f'<1,2> Opcodes: {str(opcodes[ptr:ptr+3]):<20} Operands: {operands}, destination_ptr: {destination_ptr}')
            opcodes[destination_ptr] = op(*operands)
            ptr += 4
        elif opcode == 3:
            operands = get_operands(opcodes, ptr+1, modes, 1)
            destination_ptr = int(opcodes[ptr+1])
            logger.debug(f'<3> Opcodes: {str(opcodes[ptr:ptr+2]):<20} Operands: {operands}, destination_ptr: {destination_ptr}')
            opcodes[operands[0]] = int(stdin.read())
            logger.debug(f'<3> Read {opcodes[operands[0]]} from input stream')
            ptr += 2
        elif opcode == 4:
            operands = get_operands(opcodes, ptr+1, modes, 1)
            logger.debug(f'<4> Opcodes: {str(opcodes[ptr:ptr+2]):<20} Operands: {operands}')
            stdout.write(operands[0])
            ptr += 2
        else:
            break

if __name__ == '__main__':
    with open('day_5.txt') as f:
        intcodes = f.read().split(',')
        # intcodes = ['1002', '4', '3', '4', '33']
        intcodes = [int (i) for i in intcodes]
        logger.info(f'First codes: {str(intcodes[:10])}')
        run(intcodes)
