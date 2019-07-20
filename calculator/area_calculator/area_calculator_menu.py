from area_calculator import area_of_triangle_calculator
from area_calculator import area_of_disk_calculator
from area_calculator import area_of_square_or_rectangle
from area_calculator import area_of_quadrilateral_calculator


def area_of_triangle_calculator_menu():
    triangle_calculator_menu_dict = {
        '1': area_of_triangle_calculator.
        calculate_and_print_area_of_triangle_by_three_sides,
        '2': area_of_triangle_calculator.
        calculate_and_print_area_of_triangle_by_two_sides_and_degree,
        '3': area_of_triangle_calculator.
        calculate_and_print_area_of_triangle_by_side_and_altitude
    }
    print('Select what you want to do\n'
          '1 - calculate by three sides\n'
          '2 - calculate by two sides and degree\n'
          '3 - calculate by side and altitude')
    inp = input()
    triangle_calculator_menu_dict.get(inp, area_of_triangle_calculator_menu)()


def area_of_quadrilateral_calculator_menu():
    quadrilateral_calculator_menu_dict = {
        '1': area_of_quadrilateral_calculator.
        calculate_and_print_area_of_quad_by_half_perimeter_and_r_of_incircle,
        '2': area_of_quadrilateral_calculator.
        calculate_and_print_area_of_quad_by_diagonals_and_degree_between
    }
    print('Select what you want to do\n'
          '1 - calculate by half perimeter and radius of incircle\n'
          '2 - calculate by diagonals and degree between')
    inp = input()
    quadrilateral_calculator_menu_dict.get(
        inp, area_of_quadrilateral_calculator_menu)()


def area_calculator_menu():
    main_menu_dict = {
        '1': area_of_triangle_calculator_menu,
        '2': area_of_disk_calculator.
        calculate_and_print_area_of_disk,
        '3': area_of_square_or_rectangle.
        calculate_and_print_area_of_square_or_rectangle,
        '4': area_of_quadrilateral_calculator_menu
    }
    print('Select what you want to do\n'
          '1 - open triangle area calculator\n'
          '2 - open disk area calculator\n'
          '3 - open square and rectangle area calculator\n'
          '4 - open quadrilateral area calculator')
    inp = input()
    main_menu_dict.get(inp, area_calculator_menu)()


if __name__ == '__main__':
    area_calculator_menu()
