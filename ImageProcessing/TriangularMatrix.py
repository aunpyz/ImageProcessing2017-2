def ComputeW(grid: list, disGrid: list, dimension: int):
    col = dimension+1
    for i in range(dimension):
        for j in range(dimension):
            m = [[grid[i*col+j][0], grid[i*col+j][1], grid[i*col+j][0]*grid[i*col+j][1], 1],
                 [grid[i*col+j+1][0], grid[i*col+j+1][1],
                     grid[i*col+j+1][0]*grid[i*col+j+1][1], 1],
                 [grid[(i+1)*col+j][0], grid[(i+1)*col+j][1],
                  grid[(i+1)*col+j][0]*grid[(i+1)*col+j][1], 1],
                 [grid[(i+1)*col+j+1][0], grid[(i+1)*col+j+1][1], grid[(i+1)*col+j+1][0]*grid[(i+1)*col+j+1][1], 1]]
            lower, tfmatrix = LUDecomposition(m)


def LUDecomposition(matrix: list):
    tfmatrix, matrix = MatrixChecker(matrix)
    l10 = round(matrix[1][0]/matrix[0][0], 2)
    l20 = round(matrix[2][0]/matrix[0][0], 2)
    l30 = round(matrix[3][0]/matrix[0][0], 2)
    matrix[1] = [0, round(matrix[1][1]-matrix[0][1]*l10, 2),
                 round(matrix[1][2]-matrix[0][2]*l10, 2),
                 round(matrix[1][3]-matrix[0][3]*l10, 2)]
    matrix[2] = [0, round(matrix[2][1]-matrix[0][1]*l20, 2),
                 round(matrix[2][2]-matrix[0][2]*l20, 2),
                 round(matrix[2][3]-matrix[0][3]*l20, 2)]
    matrix[3] = [0, round(matrix[3][1]-matrix[0][1]*l30, 2),
                 round(matrix[3][2]-matrix[0][2]*l30, 2),
                 round(matrix[3][3]-matrix[0][3]*l30, 2)]
    l21 = round(matrix[2][1]/matrix[1][1], 2)
    l31 = round(matrix[3][1]/matrix[1][1], 2)
    matrix[2] = [0, 0, round(matrix[2][2]-matrix[1][2]*l21, 2),
                 round(matrix[2][3]-matrix[1][3]*l21, 2)]
    matrix[3] = [0, 0, round(matrix[3][2]-matrix[1][2]*l31, 2),
                 round(matrix[3][3]-matrix[1][3]*l31, 2)]
    l32 = round(matrix[3][2]/matrix[2][2], 2)
    matrix[3] = [0, 0, 0, round(matrix[3][3]-matrix[2][3]*l32, 2)]
    lower = [[1, 0, 0, 0],
             [l10, 1, 0, 0],
             [l20, l21, 1, 0],
             [l30, l31, l32, 1]]
    return lower, tfmatrix


def MatrixChecker(matrix: list):
    tfmatrix = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    if matrix[0][0] == 0:
        for i in range(1, 4):
            if matrix[i][0] != 0:
                tmp = tfmatrix[0]
                tfmatrix[0] = tfmatrix[i]
                tfmatrix[i] = tmp
                tmp = matrix[0]
                matrix[0] = matrix[i]
                matrix[i] = tmp
                break
    if matrix[1][1] == 0:
        for i in range(2, 4):
            if matrix[i][1] != 0:
                tmp = tfmatrix[1]
                tfmatrix[1] = tfmatrix[i]
                tfmatrix[i] = tmp
                tmp = matrix[1]
                matrix[1] = matrix[i]
                matrix[i] = tmp
                break
    if matrix[2][2] == 0:
        tmp = tfmatrix[2]
        tfmatrix[2] = tfmatrix[3]
        tfmatrix[3] = tmp
        tmp = matrix[2]
        matrix[2] = matrix[3]
        matrix[3] = tmp
    return tfmatrix, matrix
