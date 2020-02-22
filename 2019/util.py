'''Common utility functions for all riddles'''

def read_input_file(number):
    with open(f'day_{number:02}.txt') as f:
        return [line.strip() for line in f.read().splitlines()]
