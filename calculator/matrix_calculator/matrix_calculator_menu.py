from matrix_calculator import (matrix_calculator, matrix_transposer)


def matrix_calculator_menu():
    matrix_calculator_menu_dict = {
        '1': matrix_calculator.sum_and_print_matrix,
        '2': matrix_calculator.multiply_and_print_matrix_by_number,
        '3': matrix_calculator.multiply_and_print_two_matrix,
        '4': matrix_calculator.print_matrix_to_the_power_of_number,
        '5': matrix_transposer.print_and_transpose_matrix
    }
    print('Select what you want to do\n'
          '1 - sum matrix\n'
          '2 - multiply matrix by a number\n'
          '3 - multiply matrix by a matrix\n'
          '4 - matrix to a power of number\n'
          '5 - transpose matrix')
    inp = input()
    matrix_calculator_menu_dict.get(inp, matrix_calculator_menu)()


if __name__ == '__main__':
    matrix_calculator_menu()
