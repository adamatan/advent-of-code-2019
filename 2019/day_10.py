#!/usr/bin/env python3

'''
Solve the day 10 riddle from Advent of Code 2019.
See https://adventofcode.com/2019/day/10
'''

import math
import json
from util import read_input_file

def parse_input(input_string):
    '''Parses the input multi-line string into a list of (x,y) tuples
    with astroid coordinates.
    The top leftmost spot is (0, 0), the spot next to it to thr right
    is (1, 0)'''
    astroid_list = list()
    for y, line in enumerate(input_string):
        for x, char in enumerate(line.strip()):
            if char == '#':
                astroid_list.append((x, y))
    return tuple(astroid_list)

def calculate_angle(astroid_a, astroid_b):
    '''Calculates the angle, in radians, from astroid_a to astroid_b.
    astroid_a can not be identical to astroid_b.'''
    assert astroid_a != astroid_b
    return math.atan2(astroid_b[0]-astroid_a[0], astroid_b[1]-astroid_a[1])

def count_visible_neighbours(origin_astroid, astroids_list):
    '''Counts the number of astroids in astroids_list visible from the
    origin astroid.
    A neighbour astroid is considered visible if there is no other
    astroid in the same angle and shorter distance blocking the eye sight
    from the origin astroid.'''
    angles = set()
    for current_astroid in astroids_list:
        if current_astroid == origin_astroid:
            continue
        angle = calculate_angle(current_astroid, origin_astroid)
        angles.add(angle)
    return len(angles)

def solve_step_1(astroids):
    return max([count_visible_neighbours(astroid, astroids) for astroid in astroids])

def solve():
    input_file_string = read_input_file(10)
    astroids = parse_input(input_file_string)
    return {
        'step_1': solve_step_1(astroids)
    }

if __name__ == '__main__':
    print(json.dumps(solve(), indent=2))
