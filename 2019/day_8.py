#!/usr/bin/env python3

import json

INPUT_FILENAME = 'day_8.txt'
INPUT_HEIGHT = 6
INPUT_WIDTH = 25

def get_layers(pixels, height, width):
    '''Returns a list of even-sized height*width sized chunks of pixels
    see https://stackoverflow.com/a/312464/51197'''
    rv = []
    index = 0
    layer_size = height * width
    while index < len(pixels):
        rv.append(pixels[index:index+layer_size])
        index += layer_size
    return rv

def solve_step_1(pixels, height, width):
    '''Returns the numerical solution to step 1 - the 1's count times
    2's count in the layer with the least number of 0's.'''
    layers = get_layers(pixels, height, width)
    layers.sort(key=lambda k:k.count('0'))
    return(layers[0].count('1') * layers[0].count('2'))

def merge_layers(pixels, height, width):
    '''Combines multiple image layers into one. Transparent pixels
    in upper layers take the color of the highest colored pixel
    in deeper layers.'''
    layers = get_layers(pixels, height, width)
    
    combined_layer = list(layers[0])
    for layer in layers[1:]:
        for index in range(len(layer)):
            if combined_layer[index] == '2':
                combined_layer[index] = layer[index]
    return combined_layer

def print_layer(layer, height, width):
    '''Prints a character image representation of a layer.
    Pixels with value 1 are black, others are transparent.'''
    for i in range(height):
        row = layer[width*i:width*(i+1)]
        row = [' ' if c != '1' else '*' for c in row]
        print(''.join(row))

def solve_step_2(pixels, height, width):
    return merge_layers(pixels, height, width)

def parse_input():
    '''Parses the input file into an array of pixels'''
    with open(INPUT_FILENAME) as f:
        return [c for c in f.read() if c.strip()]

if __name__ == '__main__':
    PIXELS = parse_input()
    print('step1:', solve_step_1(PIXELS, INPUT_HEIGHT, INPUT_WIDTH))
    print('step2:')
    output_image = solve_step_2(PIXELS, INPUT_HEIGHT, INPUT_WIDTH)
    print_layer(output_image, INPUT_HEIGHT, INPUT_WIDTH)