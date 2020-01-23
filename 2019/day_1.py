#!/usr/bin/env python3

import json

def solve_step_1(lines):
    masses = [int(s) for s in lines]
    fuel_intakes = [m//3-2 for m in masses if m > 0]
    return (sum(fuel_intakes))

def calculate_fuel_intake_step_2(mass):
    if mass > 0:
        return max(0, mass//3-2 + calculate_fuel_intake_step_2(mass//3-2))
    return 0

def solve_step_2(lines):
    masses = [int(s) for s in lines]
    fuel_intakes = [calculate_fuel_intake_step_2(m) for m in masses if m > 0]
    return (sum(fuel_intakes))

if __name__ == '__main__':
    with open('day_1.txt') as f:
        lines = f.read().split()
    rv = {
        'step1': solve_step_1(lines),
        'step2': solve_step_2(lines)
    }
    print(json.dumps(rv, indent=2))

