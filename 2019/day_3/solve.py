#!/usr/bin/env python3
from operator import add


DIRECTIONS = {
    'D': (0, -1),
    'U': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

def get_wire_coordinates(wire):
    '''Returns a set of coordinates covered by the wire'''
    point = (0, 0)
    coordinates = set([point])
    for path in wire:
        direction = path[0]
        length = int(path[1:])
        for _ in range(length):
            point = tuple(map(add, DIRECTIONS[direction], point))
            coordinates.add(point)
    return(coordinates)

def manhattan(point):
    '''Manhattan distance from a point to (0, 0)'''
    return abs(point[0]) + abs(point[1])

def solve(wire_1, wire_2):
    path_1, path_2 = get_wire_coordinates(wire_1), get_wire_coordinates(wire_2)
    intersections = path_1.intersection(path_2 - {(0,0)})
    rv = min(list(map(manhattan, intersections)))
    return rv

if __name__ == '__main__':
    with open('input.txt') as f:
        WIRES = [line.strip().split(',') for line in f]
    print(solve(*WIRES))
