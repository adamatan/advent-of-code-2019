#!/usr/bin/env python3

import io
from operator import add, mul, le, eq
import sys
import logging
import json

logger = logging.getLogger('root')
FORMAT = "[%(funcName)30s() ]   %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.ERROR)


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
        logger.info(f'ptr: {ptr}, codes [{ptr}:{ptr+10}]: {str(intcodes[ptr:ptr+10])}')
        logger.debug(f'ptr: {ptr}, intcodes[ptr]: {intcodes[ptr]}')
        opcode, modes = parse_opcode_and_modes(operator)
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
            predicate = True if opcode == 5 else False
            operands = get_operands(intcodes, ptr+1, modes, 2)
            logger.debug(f'<5,6> intcodes: {str(intcodes[ptr:ptr+2]):<20} Operands: {operands}')
            if bool(operands[0]) == predicate:
                ptr = operands[1]
            else:
                ptr += 3
        elif opcode in(7, 8):
            operator = le if opcode ==7 else eq
            operands = get_operands(intcodes, ptr+1, modes, 3)
            logger.debug(f'<7,8> intcodes: {str(intcodes[ptr:ptr+3]):<20} Operands: {operands}')
            if operator(operands[0], operands[1]):
                ptr = operands[2]
            else:
                ptr += 4

        else:
            break

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
    stdin = io.StringIO('0')
    stdout = io.StringIO()
    run(intcodes, stdin=stdin, stdout=stdout)
    step_2 = int(stdout.getvalue().split()[-1])
    return step_2

if __name__ == '__main__':
    FILENAME = 'day_5.txt'
    intcodes = parse_intcodes(FILENAME)
    intcodes = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    rv = {
        'step1': run_step_1(intcodes),
        'step2': run_step_2(intcodes)
    }
    print(json.dumps(rv, indent=2))