#!/usr/bin/env python3

import json
import logging
from collections import defaultdict

SUN = 'COM'
INPUT_FILENAME = 'day_6.txt'

logger = logging.getLogger('root')
FORMAT = "[%(funcName)30s() ]   %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.INFO)


def get_input_data(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]

def parse(input_data):
    '''Parse the raw text into a dictionary mapping a sun to a 
    list of plants orbiting it.'''
    orbits_map = defaultdict(list)
    orbits_map_symmetric = defaultdict(list)
    for line in input_data:
        sun, planet = line.split(')')
        orbits_map[sun].append(planet)
        orbits_map_symmetric[sun].append(planet)
        orbits_map_symmetric[planet].append(sun)
    return orbits_map, orbits_map_symmetric


def count_orbit_pairs(orbits_map, source_node, current_depth=0):
    '''Counts the number of direct and indirect orbit relations between
    planets.'''
    count = 0
    if planets := orbits_map.get(source_node):
        for planet in planets:
            count += count_orbit_pairs(orbits_map, planet, current_depth+1)
    return current_depth + count

def bfs(orbits_map, source_node, destination_node):
    visiting = [(source_node, 0)]
    exhausted = set()
    depth = 0
    while visiting:
        current_node, depth = visiting.pop(0)
        logger.debug(f'Visiting {current_node:<7}, depth is {depth:<5}, visiting={visiting}, exhausted={exhausted}')
        exhausted.add(current_node)
        if current_node == destination_node:
            return depth - 2
        if neighbours := orbits_map.get(current_node):
            for neighbour in neighbours:
                if neighbour not in exhausted:
                    visiting.append((neighbour, depth+1))
        depth += 1
    return None


if __name__ == '__main__':
    input_data = get_input_data(INPUT_FILENAME)
    orbits, symmetric_orbits = parse(input_data)
    rv = {
        'step_1': count_orbit_pairs(orbits, SUN),
        'step_2': bfs(symmetric_orbits, 'YOU', 'SAN')
    }
    print(json.dumps(rv, indent=2))