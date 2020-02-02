#!/usr/bin/env python3

import io
from operator import add, mul, lt, eq
import sys
import logging
import json

logger = logging.getLogger('root')
FORMAT = "[%(funcName)30s() ]   %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


def parse_opcode_and_modes(operator):
    padded_operator = str(operator)
    padded_operator = '0' * (5-len(padded_operator)) + padded_operator
    opcode = int(padded_operator[3:])
    modes = [int(i) for i in padded_operator[:3]]
    logger.debug(f'Operator: {operator:<5}'
                 f'Padded operator: {padded_operator:<10}'
                 f'Opcode: {opcode:<5}'
                 f'Modes: {str(modes):<10}')
    modes.reverse()
    return opcode, modes

def get_operand(intcodes, ptr, mode):
    if int(mode) == 0:
        rv = intcodes[intcodes[ptr]]
    else:
        rv = int(intcodes[ptr])
    logger.debug(f'Operand: {rv:<6}, mode: {mode}, ptr: {ptr}')
    return rv

def get_operands(intcodes, ptr, modes, count):
    rv = []
    for i in range(count):
        rv.append(get_operand(intcodes, ptr+i, modes[i]))
    return rv

def run(intcodes, stdin=sys.stdin, stdout=sys.stdout):
    ptr = 0
    while (operator := intcodes[ptr]) != 99 and (ptr < len(intcodes)):
        opcode, modes = parse_opcode_and_modes(operator)
        logger.info(f'NEW CYCLE: ptr: {ptr}, intcodes[ptr]: {intcodes[ptr]}, codes [{ptr}:{ptr+10}]: {str(intcodes[ptr:ptr+10])}')
        if opcode in (1, 2):
            op = mul if opcode == 2 else add
            operands = get_operands(intcodes, ptr+1, modes, 2)
            destination_ptr = int(intcodes[ptr+3])
            logger.debug(f'<1,2> intcodes: {str(intcodes[ptr:ptr+3]):<20} Operands: {operands}, destination_ptr: {destination_ptr}')
            intcodes[destination_ptr] = op(*operands)
            ptr += 4
        elif opcode == 3:
            destination_ptr = int(intcodes[ptr+1])
            logger.debug(f'<3> intcodes: {str(intcodes[ptr:ptr+2]):<20} destination_ptr: {destination_ptr}')
            intcodes[destination_ptr] = int(stdin.read())
            logger.debug(f'<3> Read {intcodes[destination_ptr]} from input stream')
            ptr += 2
        elif opcode == 4:
            operands = get_operands(intcodes, ptr+1, modes, 1)
            logger.debug(f'<4> intcodes: {str(intcodes[ptr:ptr+2]):<20} Operands: {operands}')
            stdout.write(str(operands[0])+'\n')
            ptr += 2
        elif opcode in(5, 6):
            predicate = opcode == 5
            operands = get_operands(intcodes, ptr+1, modes, 2)
            logger.debug(f'<5,6> intcodes: {str(intcodes[ptr:ptr+2]):<20} Operands: {operands}')
            if bool(operands[0]) == predicate:
                ptr = operands[1]
                logger.debug(f'ptr set to {ptr}, value is {intcodes[ptr]}')
            else:
                ptr += 3
        elif opcode in(7, 8):
            operator = lt if opcode == 7 else eq
            operands = get_operands(intcodes, ptr+1, modes, 3)
            logger.debug(f'<7,8> intcodes: {str(intcodes[ptr:ptr+3]):<20} Operands: {operands}')
            intcodes[operands[2]] = 1 if operator(operands[0], operands[1]) else 0
            ptr += 4
        else:
            raise ValueError(f'Opcode {opcode} is unknown')

def parse_intcodes(filename):
    with open(filename) as f:
        intcodes = f.read().split(',')
    return [int(i) for i in intcodes]


def run_step_1(intcodes):
    stdin = io.StringIO('1')
    stdout = io.StringIO()
    run(intcodes, stdin=stdin, stdout=stdout)
    return int(stdout.getvalue().split()[-1])

def run_step_2(intcodes):
    stdin = io.StringIO('5')
    stdout = io.StringIO()
    run(intcodes, stdin=stdin, stdout=stdout)
    return int(stdout.getvalue().split()[-1])

if __name__ == '__main__':
    FILENAME = 'day_5.txt'
    file_intcodes = parse_intcodes(FILENAME)
    rv = {
        'step1': run_step_1(list(file_intcodes)),
        'step2': run_step_2(list(file_intcodes))
    }
    print(json.dumps(rv, indent=2))