#!/usr/bin/env python3
from operator import add, mul

with open('input.txt') as f:
    INTCODES = [int(i) for i in f.read().split(',')]

def run_program(intcodes):
    i = 0
    while i<len(intcodes):
        if intcodes[i] == 99:
            break
        elif intcodes[i] == 1:
            operator = add
        elif intcodes[i] == 2:
            operator = mul
        else:
            raise ValueError(f'Opcode expected to be 1 or 2, found {intcodes[i]}')
        operands = intcodes[intcodes[i+1]], intcodes[intcodes[i+2]]
        intcodes[intcodes[i+3]] = operator(*operands)
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

print(f'Part 1: {part_1()}')
print(f'Part 2: {part_2()}')