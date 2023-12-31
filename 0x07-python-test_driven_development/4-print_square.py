#!/usr/bin/python3
'''A function that prints a square with the character #
'''


def print_square(size):
    '''Prints a square with the character '#'.

    Args:
        size (int): The size length of the square.
    '''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for i in range(size):
            print('{}'.format('#' * size))
