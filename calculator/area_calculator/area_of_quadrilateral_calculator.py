from utils import *
import math


def calculate_area_of_quad_by_half_perimeter_and_r_of_incircle(p, r):
    result = p*r
    return result


def calculate_area_of_quad_by_diagonals_and_degree_between(d1, d2, degree):
    result = (1/2)*d1*d2*math.sin(math.radians(degree))
    return result


def calculate_and_print_area_of_quad_by_half_perimeter_and_r_of_incircle():
    p = input('Enter half perimeter of a quadrilateral ')
    if str_to_float_or_int_converter(p):
        p = str_to_float_or_int_converter(p)
        if p > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False
    r = input('Enter radius of incircle ')
    if str_to_float_or_int_converter(r) and can_continue:
        r = str_to_float_or_int_converter(r)
        if r > 0:
            can_continue = True
        else:
            can_continue = False
    if can_continue:
        print('Area of quadrilateral is ' +
              str(calculate_area_of_quad_by_half_perimeter_and_r_of_incircle(
                  p, r)))
    else:
        print('Error half perimeter and radius be a numbers that higher than 0'
              '')
        calculate_and_print_area_of_quad_by_half_perimeter_and_r_of_incircle()


def calculate_and_print_area_of_quad_by_diagonals_and_degree_between():
    d1 = input('Input first diagonal of a quadrilateral ')
    if str_to_float_or_int_converter(d1):
        d1 = str_to_float_or_int_converter(d1)
        if d1 > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False
    d2 = input('Input second diagonal of a quadrilateral ')
    if str_to_float_or_int_converter(d2) and can_continue:
        d2 = str_to_float_or_int_converter(d2)
        if d2 > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False
    deg = input('Input degree between diagonals ')
    if str_to_float_or_int_converter(deg) and can_continue:
        deg = str_to_float_or_int_converter(deg)
        if deg > 0:
            can_continue = True
        else:
            can_continue = False
    else:
        can_continue = False
    if can_continue:
        print('Area of quadrilateral is ' +
              str(calculate_area_of_quad_by_diagonals_and_degree_between(
                  d1, d2, deg)))
    else:
        print('Error diagonals and degree'
              ' must be a numbers that higher than 0')
        calculate_and_print_area_of_quad_by_diagonals_and_degree_between()


if __name__ == '__main__':
    print(calculate_area_of_quad_by_half_perimeter_and_r_of_incircle(4, 2))
    print(calculate_area_of_quad_by_diagonals_and_degree_between(2, 2, 30))
    calculate_and_print_area_of_quad_by_half_perimeter_and_r_of_incircle()
