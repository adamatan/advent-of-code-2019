#!/usr/bin/env python3
from operator import add, mul

with open('input.txt') as f:
    INTCODES = [int(i) for i in f.read().split(',')]

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

def part_1():
    intcodes = list(INTCODES)
    # "To do this, before running the program, replace position 1 with the 
    # value 12 and replace position 2 with the value 2."
    intcodes[1], intcodes[2] = 12, 2
    return run_program(intcodes)

def part_2():
    for i in range(100):
        for j in range(100):
            intcodes = list(INTCODES)
            intcodes[1], intcodes[2] = i, j
            if run_program(intcodes) == 19690720:
                return(100*i+j)
# Part 1: 5110675
# Part 2: 4847
print(f'Part 1: {part_1()}')
print(f'Part 2: {part_2()}')