import math
from utils import *


def calculate_area_of_triangle_by_three_sides(a, b, c):
    p = (a + b + c)/2  # half_perimeter
    result = math.sqrt(p*(p-a)*(p-b)*(p-c))
    if result > 0:
        return result
    else:  # comment this if you want only raw output
        return 'uncalculatable'


def calculate_area_of_triangle_by_two_sides_and_degree(a, b, d):
    sin = math.sin(math.radians(d))
    result = (a*b*sin)/2
    return result


def calculate_area_of_triangle_by_side_and_altitude(a, s):
    return (s*a)/2


def calculate_and_print_area_of_triangle_by_three_sides():
    a = input('Input first triangle side ')
    if str_to_float_or_int_converter(a):
        a = str_to_float_or_int_converter(a)
        if a > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False

    b = input('Input second triangle side ')
    if str_to_float_or_int_converter(b) and can_continue:
        b = str_to_float_or_int_converter(b)
        if b > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False

    c = input('Input third triangle side ')
    if str_to_float_or_int_converter(c) and can_continue:
        c = str_to_float_or_int_converter(c)
        if c > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False

    if can_continue:
        print('Area of triangle is '+str(
            calculate_area_of_triangle_by_three_sides(a, b, c)))
    else:
        print('Error sides must be a positive numbers that higher than 0')
        calculate_and_print_area_of_triangle_by_three_sides()


def calculate_and_print_area_of_triangle_by_two_sides_and_degree():
    a = input('Input first triangle side ')
    if str_to_float_or_int_converter(a):
        a = str_to_float_or_int_converter(a)
        if a > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False

    b = input('Input second triangle side ')
    if str_to_float_or_int_converter(b) and can_continue:
        b = str_to_float_or_int_converter(b)
        if b > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False
    d = input('Input degree ')
    if str_to_float_or_int_converter(d) and can_continue:
        d = str_to_float_or_int_converter(d)
        if d > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False

    if can_continue:
        print('Area of triangle is '+str(
            calculate_area_of_triangle_by_two_sides_and_degree(a, b, d)))
    else:
        print('Error side or degree must be a '
              'positive number that higher than 0')
        calculate_and_print_area_of_triangle_by_two_sides_and_degree()


def calculate_and_print_area_of_triangle_by_side_and_altitude():
    s = input('Input triangle side ')
    if str_to_float_or_int_converter(s):
        s = str_to_float_or_int_converter(s)
        if s > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False
    a = input('Input altitude of that side ')
    if str_to_float_or_int_converter(a) and can_continue:
        a = str_to_float_or_int_converter(a)
        if a > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False

    if can_continue:
        print('Area of triangle is '+str(
            calculate_area_of_triangle_by_side_and_altitude(a, s)))
    else:
        print('Error side and altitude must be a '
              'positive number that higher than 0')
        calculate_and_print_area_of_triangle_by_two_sides_and_degree()


if __name__ == '__main__':
    calculate_and_print_area_of_triangle_by_three_sides()
    calculate_and_print_area_of_triangle_by_two_sides_and_degree()
    calculate_and_print_area_of_triangle_by_side_and_altitude()
