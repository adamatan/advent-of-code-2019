#!/usr/bin/env python3

'''
Solve the day 10 riddle from Advent of Code 2019.
See https://adventofcode.com/2019/day/10
'''

class Moon(object):
    def __init__(self, x, y, z):
        self.position = [x, y, z]
        self.velocity = [0, 0, 0]

    def apply_velocity(self):
        self.position = [p+v for p,v in zip(self.position, self.velocity)]

    def set_gravity(self, other_moons):
        for other_moon in other_moons:
            for axis in (0, 1, 2):
                if self.position[axis] < other_moon.position[axis]:
                    self.velocity[axis] += 1
                elif self.position[axis] > other_moon.position[axis]:
                    self.velocity[axis] -= 1

    @property
    def energy(self):
        potential = sum([abs(p) for p in self.position])
        kinetic = sum([abs(v) for v in self.velocity])
        return potential * kinetic

    def __str__(self):
        return f'pos=<x={self.position[0]:3}, '+\
                    f'y={self.position[1]:3}, '+\
                    f'z={self.position[2]:3}>, '+\
               f'vel=<x={self.velocity[0]:3}, '+\
                    f'y={self.velocity[1]:3}, '+\
                    f'z={self.velocity[2]:3}>'

moons_1 = (
    Moon(-1, 0, 2),
    Moon(2, -10, -7),
    Moon(4, -8, 8),
    Moon(3, 5, -1)
)

moons_2 = (
    Moon(-8, -10, 0),
    Moon(5, 7, 10),
    Moon(2, -7, 3),
    Moon(9, -8, -3)
)

moons = moons_2

for step in range(101):
    print(f'After step {step}')
    for moon in moons:
        print(moon)
    for moon in moons:
        others = (other for other in moons if other != moon)
        moon.set_gravity(others)
    for moon in moons:
        moon.apply_velocity()

print(sum([moon.energy for moon in moons]))
