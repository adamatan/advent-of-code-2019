#!/usr/bin/env python3

import json
from operator import add, mul

OPERATORS = {
    1: add,
    2: mul
}

def run_program(intcodes):
    i = 0
    while (intcodes[i] != 99 and i<len(intcodes)-4):
        operator = OPERATORS[intcodes[i]]
        destination_pointer = intcodes[i+3]
        operand1, operand2 = intcodes[intcodes[i+1]], intcodes[intcodes[i+2]]
        intcodes[destination_pointer] = operator(operand1, operand2)
        i+=4

    return(intcodes[0])

def solve_step_1(intcodes):
    cur_intcodes = list(intcodes)
    # "To do this, before running the program, replace position 1 with the 
    # value 12 and replace position 2 with the value 2."
    cur_intcodes[1], cur_intcodes[2] = 12, 2
    return run_program(cur_intcodes)

def solve_step_2(intcodes):
    for i in range(100):
        for j in range(100):
            cur_intcodes = list(intcodes)
            cur_intcodes[1], cur_intcodes[2] = i, j
            if run_program(cur_intcodes) == 19690720:
                return(100*i+j)


if __name__ == '__main__':
    with open('day_2.txt') as f:
        intcodes = [int(i) for i in f.read().split(',')]

    rv = {
        'step1': solve_step_1(intcodes),
        'step2': solve_step_2(intcodes)
    }
    print(json.dumps(rv, indent=2))
