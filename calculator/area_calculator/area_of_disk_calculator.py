import math
from utils import *


def calculate_area_of_disk(r):
    return math.pi*r**2


def calculate_and_print_area_of_disk():
    r = input('Input radius of a disk ')
    if str_to_float_or_int_converter(r):
        r = str_to_float_or_int_converter(r)
        if r > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False
    if can_continue:
        print('Area of disk is '+str(calculate_area_of_disk(r)))
    else:
        print('Error radius must be a number that higher than 0')
        calculate_and_print_area_of_disk()


if __name__ == '__main__':
    calculate_and_print_area_of_disk()
