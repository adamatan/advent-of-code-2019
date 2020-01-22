#!/usr/bin/env python3
'''
Solves "Day 3: Crossed Wires" from adventofcode.com.
'''

from operator import add

def get_wire_coordinates(wire):
    '''Returns a list of coordinates covered by the wire. A wire is a list of
    directions and distances originating from (0, 0).
    For example, ['R8','U5','L5','D3'] should return [ (0,0), (1, 0), (2, 0) ...]'''
    DIRECTIONS = {
        'D': (0, -1),
        'U': (0, 1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    point = (0, 0)
    coordinates = [point]
    for path in wire:
        direction = path[0]
        length = int(path[1:])
        for _ in range(length):
            point = tuple(map(add, DIRECTIONS[direction], point))
            coordinates.append(point)
    return(coordinates)

def manhattan(point):
    '''Manhattan distance from a point to (0, 0)'''
    return abs(point[0]) + abs(point[1])


def get_intersection(path_1, path_2):
    '''Returns a set of interesecting coordinates between two paths'''
    intersections = set(path_1).intersection(set(path_2) - {(0,0)})
    return intersections

def solve_step_1(wire_1, wire_2):
    '''Returns the Manhattan distance of the intersection nearest to (0, 0)'''
    path_1, path_2 = get_wire_coordinates(wire_1), get_wire_coordinates(wire_2)
    intersections = get_intersection(path_1, path_2)
    rv = min(list(map(manhattan, intersections)))
    return rv

def solve_step_2(wire_1, wire_2):
    '''Returns the intersection whose combined traverse distance is minimal.
    The combined traverse distance is the combined wire length from the origin
    to the intersection.'''
    path_1, path_2 = get_wire_coordinates(wire_1), get_wire_coordinates(wire_2)
    intersections = get_intersection(path_1, path_2)
    distances = [path_1.index(intersection)+path_2.index(intersection) for intersection in intersections]
    return(min(distances))
    
if __name__ == '__main__':
    with open('input.txt') as f:
        WIRES = [line.strip().split(',') for line in f]
    print(solve_step_1(*WIRES))
