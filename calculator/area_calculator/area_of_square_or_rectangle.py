from utils import *


def calculate_area_of_rectangle(a, b):
    return a*b


def calculate_area_of_square(s):
    return s**2


def calculate_and_print_area_of_square_or_rectangle():
    print('Select one:\n'
          '1 - area of square\n'
          '2 - area of rectangle')
    inp = input()
    if inp == '1':
        s = input('Input side of a square ')
        if str_to_float_or_int_converter(s):
            s = str_to_float_or_int_converter(s)
            if s > 0:
                can_continue = True
            else:
                can_continue = False
        else:
            can_continue = False
        if can_continue:
            print('Area of square is ' + str(calculate_area_of_square(s)))
        else:
            print('Error side must be a number that higher than 0')
            calculate_and_print_area_of_square_or_rectangle()
    elif inp == '2':
        a = input('Input first side of a rectangle ')
        if str_to_float_or_int_converter(a):
            a = str_to_float_or_int_converter(a)
            if a > 0:
                can_continue = True
            else:
                can_continue = False
        else:
            can_continue = False
        b = input('Input second side of a rectangle ')
        if str_to_float_or_int_converter(b) and can_continue:
            b = str_to_float_or_int_converter(b)
            if b > 0:
                can_continue = True
            else:
                can_continue = False
        if can_continue:
            print('Area of rectangle is ' + str(calculate_area_of_rectangle(
                a, b)))
        else:
            print('Error sides must be a numbers that higher than 0')
            calculate_and_print_area_of_square_or_rectangle()
    else:
        calculate_and_print_area_of_square_or_rectangle()
        print('Please input 1 or 2')


if __name__ == '__main__':
    calculate_and_print_area_of_square_or_rectangle()
