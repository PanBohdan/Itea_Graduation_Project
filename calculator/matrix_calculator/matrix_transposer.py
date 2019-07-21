from matrix_calculator import matrix_calculator


def matrix_transpose(matrix):
    result = [[matrix[j][i]
               for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result


def print_and_transpose_matrix():
    inp = matrix_calculator.matrix_from_input()
    print(matrix_transpose(inp))


if __name__ == '__main__':
    mat1 = [[4, 3, 2, 2],
            [1, 2, 3, 1]]
    print(matrix_transpose(mat1))
