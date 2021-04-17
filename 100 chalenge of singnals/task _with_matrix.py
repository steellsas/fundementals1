
def matrixElementsSum(matrix):
    posible_mat = []
    sum_price = 0
    is_posible = [True] * len(matrix[0])
    for row_i in range(len(matrix)):
        posible_mat.append(is_posible)
        for col_i in range(len(matrix[row_i])):
            if matrix[row_i][col_i] != 0 and posible_mat[row_i][col_i]:
                sum_price = sum_price + matrix[row_i][col_i]
            else:
                posible_mat[row_i][col_i] = False

    print(posible_mat)
    print(sum_price)

t_mat = [[1, 1, 1, 0],
               [0, 5, 0, 1],
              [2, 1, 3, 10]]
matrixElementsSum(t_mat)