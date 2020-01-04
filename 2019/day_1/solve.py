#!/usr/bin/env python3

with open('input.txt') as f:
    lines = f.read().split()

masses = [int(s) for s in lines]
fuel_intakes = [m//3-2 for m in masses if m > 0]

print(sum(fuel_intakes))
