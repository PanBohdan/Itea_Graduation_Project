from utils import (is_matched, str_to_float_or_int_converter,
                   is_number_int_or_float, is_number_float)


def is_matrix_same_size(matrix1, matrix2):
    row1 = len(matrix1)
    col1 = len(matrix1[0])
    row2 = len(matrix2)
    col2 = len(matrix2[1])
    if row1 == row2 and col1 == col2:
        return True
    else:
        return False


def sum_matrix(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j]
               for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result


def multiply_two_matrix(matrix1, matrix2):
    result = [[matrix1[i][j] * matrix2[i][j]
               for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result


def multiply_matrix_by_number(matrix, number):
    result = [[matrix[i][j] * number
               for j in range(len(matrix[0]))] for i in range(len(matrix))]
    return result


def matrix_to_the_power_of_number(matrix, number):
    result = [[matrix[i][j] ** number
               for j in range(len(matrix[0]))] for i in range(len(matrix))]
    return result


def matrix_from_input():
    row_num = row_input()
    while not row_num:
        row_num = row_input()
    col_num = col_input()
    while not col_num:
        col_num = col_input()
    matrix = []
    for i in range(row_num):
        a = []
        for j in range(col_num):
            inp = input('Enter '+str(i+1)+' row '+str(j+1)+' column ')
            if is_number_int_or_float(inp):
                inp = str_to_float_or_int_converter(inp)
                a.append(inp)
            else:
                print('Input must be a number')
                return False
        matrix.append(a)
    return matrix


def row_input():
    row_num = input('Input the number of rows: ')
    if not is_number_float(row_num):
        if is_number_int_or_float(row_num):
            row_num = int(row_num)
            if not row_num > 0:
                print('Number of rows must be a'
                      ' positive integer that larger than 0')
                return False
            return row_num
        else:
            print('Number of rows must be a'
                  ' positive integer that larger than 0')
            return False
    else:
        print('Number of rows must be a'
              ' positive integer that larger than 0')
        return False


def col_input():
    col_num = input('Input the number of columns: ')
    if not is_number_float(col_num):
        if is_number_int_or_float(col_num):
            col_num = int(col_num)
            if not col_num > 0:
                print('Number of columns must be a'
                      ' positive integer that larger than 0')
                return False
            return col_num
        else:
            print('Number of columns must be a'
                  ' positive integer that larger than 0')
            return False
    else:
        print('Number of rows must be a positive integer that larger than 0')
        return False


def sum_and_print_matrix():
    print('Enter the two matrix you want to sum')
    inp1 = matrix_from_input()
    while not inp1:
        inp1 = matrix_from_input()
    if is_matched(inp1):
        can_continue = True
    else:
        can_continue = False

    inp2 = matrix_from_input()
    while not inp2:
        inp2 = matrix_from_input()
    if is_matched(inp2) and can_continue:
        can_continue = True
    if can_continue:
        print(sum_matrix(inp1, inp2))


def multiply_and_print_two_matrix():
    print('Enter the two matrix you want to multiply')
    inp1 = matrix_from_input()
    while not inp1:
        inp1 = matrix_from_input()
    if is_matched(inp1):
        can_continue = True
    else:
        can_continue = False

    inp2 = matrix_from_input()
    while not inp2:
        inp2 = matrix_from_input()
    if is_matched(inp2) and can_continue:
        can_continue = True
    if can_continue:
        print(multiply_two_matrix(inp1, inp2))


def multiply_and_print_matrix_by_number():
    print('Enter the matrix you want to multiply')
    inp1 = matrix_from_input()
    while not inp1:
        inp1 = matrix_from_input()
    if is_matched(inp1):
        can_continue = True
    else:
        can_continue = False

    inp_number = input('Enter number that you want matrix be multiplied by ')
    if is_number_int_or_float(inp_number) and can_continue:
        inp_number = str_to_float_or_int_converter(inp_number)
    else:
        can_continue = False
    if can_continue:
        print(multiply_matrix_by_number(inp1, inp_number))
    else:
        print('Matrix must be square or rectangle and number must be a number')
        multiply_matrix_by_number()


def print_matrix_to_the_power_of_number():
    print('Enter the matrix you want to multiply')
    inp1 = matrix_from_input()
    while not inp1:
        inp1 = matrix_from_input()
    if is_matched(inp1):
        can_continue = True
    else:
        can_continue = False

    inp_number = input('Enter number that you want matrix be powered by ')
    if is_number_int_or_float() and can_continue:
        inp_number = str_to_float_or_int_converter(inp_number)
    else:
        can_continue = False
    if can_continue:
        print(matrix_to_the_power_of_number(inp1, inp_number))
    else:
        print('Matrix must be square or rectangle and number must be a number')
        print_matrix_to_the_power_of_number()


if __name__ == '__main__':
    mat1 = [[4, 3, 2, 2],
            [1, 2, 3, 1]]
    mat2 = [[1, 2, 3, 4],
            [2, 3, 4, 1]]
    print(sum_matrix(mat1, mat2))
    print(multiply_two_matrix(mat1, mat2))
    print(multiply_matrix_by_number(mat1, 2))
    print(matrix_to_the_power_of_number(mat1, 2))
    sum_and_print_matrix()
