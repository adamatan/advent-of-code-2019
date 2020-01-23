#!/usr/bin/env python3
'''
Solves "Day 3: Day 4: Secure Container" from adventofcode.com.
'''

from collections import Counter
import json

def is_sorted(password):
    return ''.join(sorted(str(password))) == str(password)

def has_duplicates(password):
    return ''.join(sorted(set(str(password)))) != str(password)

def password_has_sequence_of_2(password):
    '''Returns true iff the password has at least one sequence of numbers
    whose length is exactly 2 (False for 111222: False, 112222: True)'''
    return 2 in Counter(str(password)).values()

def solve_step_1(min_pass, max_pass):
    passwords = range(min_pass, max_pass+1)
    valid_passwords = ([p for p in passwords if is_sorted(p) and has_duplicates(p)])
    return len(valid_passwords)

def solve_step_2(min_pass, max_pass):
    passwords = range(min_pass, max_pass+1)
    valid_passwords = ([p for p in passwords if \
        is_sorted(p) and \
        has_duplicates(p) and \
        password_has_sequence_of_2(p)])
    return len(valid_passwords)

if __name__ == '__main__':
    rv = {
        'step1': solve_step_1(145852, 616942),
        'step2': solve_step_2(145852, 616942)
    }
    print(json.dumps(rv, indent=2))