def ComputeW(grid: list, disGrid: list, dimension: int)->tuple:
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
            # create x' and y' vector to calculate w1-w8
            x = [disGrid[i*col+j][0],
                 disGrid[i*col+j+1][0],
                 disGrid[(i+1)*col+j][0],
                 disGrid[(i+1)*col+j+1][0]]
            y = [disGrid[i*col+j][1],
                 disGrid[i*col+j+1][1],
                 disGrid[(i+1)*col+j][1],
                 disGrid[(i+1)*col+j+1][1]]
            ax = [0, 0, 0, 0]
            ay = [0, 0, 0, 0]
            for row in range(4):
                if tfmatrix[row][0] == 1:
                    ax[0] = x[row]
                    ay[0] = y[row]
                elif tfmatrix[row][1] == 1:
                    ax[1] = x[row]
                    ay[1] = y[row]
                elif tfmatrix[row][2] == 1:
                    ax[2] = x[row]
                    ay[2] = y[row]
                else:
                    ax[3] = x[row]
                    ay[3] = y[row]

            bx = CalMatrix(ax, lower, True)
            by = CalMatrix(ay, lower, True)

            # w1-w8
            wx = CalMatrix(bx, m, False)
            wy = CalMatrix(by, m, False)
            yield wx, wy


def LUDecomposition(matrix: list):
    tfmatrix, matrix = MatrixChecker(matrix)
    l10 = round(matrix[1][0]/matrix[0][0], 5)
    l20 = round(matrix[2][0]/matrix[0][0], 5)
    l30 = round(matrix[3][0]/matrix[0][0], 5)
    matrix[1] = [0, round(matrix[1][1]-matrix[0][1]*l10, 5),
                 round(matrix[1][2]-matrix[0][2]*l10, 5),
                 round(matrix[1][3]-matrix[0][3]*l10, 5)]
    matrix[2] = [0, round(matrix[2][1]-matrix[0][1]*l20, 5),
                 round(matrix[2][2]-matrix[0][2]*l20, 5),
                 round(matrix[2][3]-matrix[0][3]*l20, 5)]
    matrix[3] = [0, round(matrix[3][1]-matrix[0][1]*l30, 5),
                 round(matrix[3][2]-matrix[0][2]*l30, 5),
                 round(matrix[3][3]-matrix[0][3]*l30, 5)]
    l21 = round(matrix[2][1]/matrix[1][1], 5)
    l31 = round(matrix[3][1]/matrix[1][1], 5)
    matrix[2] = [0, 0, round(matrix[2][2]-matrix[1][2]*l21, 5),
                 round(matrix[2][3]-matrix[1][3]*l21, 5)]
    matrix[3] = [0, 0, round(matrix[3][2]-matrix[1][2]*l31, 5),
                 round(matrix[3][3]-matrix[1][3]*l31, 5)]
    l32 = round(matrix[3][2]/matrix[2][2], 5)
    matrix[3] = [0, 0, 0, round(matrix[3][3]-matrix[2][3]*l32, 5)]
    lower = [[1, 0, 0, 0],
             [l10, 1, 0, 0],
             [l20, l21, 1, 0],
             [l30, l31, l32, 1]]
    InverseMatrix(tfmatrix)
    return lower, tfmatrix


def MatrixChecker(matrix: list)->tuple:
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


def InverseMatrix(matrix: list):
    lst = list(matrix)
    matrix[0] = [lst[0][0], lst[1][0], lst[2][0], lst[3][0]]
    matrix[1] = [lst[0][1], lst[1][1], lst[2][1], lst[3][1]]
    matrix[2] = [lst[0][2], lst[1][2], lst[2][2], lst[3][2]]
    matrix[3] = [lst[0][3], lst[1][3], lst[2][3], lst[3][3]]


def CalMatrix(vector: list, matrix: list, isLower: bool)->list:
    lst = [0, 0, 0, 0]
    if isLower:
        lst[0] = vector[0]
        lst[1] = round(vector[1]
                       - lst[0]*matrix[1][0], 5)
        lst[2] = round(vector[2]
                       - lst[0]*matrix[2][0]
                       - lst[1]*matrix[2][1], 5)
        lst[3] = round(vector[3]-lst[0]*matrix[3][0]
                       - lst[1]*matrix[3][1]
                       - lst[2]*matrix[3][2], 5)
    else:
        lst[3] = round(vector[3]
                       / matrix[3][3], 5)
        lst[2] = round((vector[2]-lst[3]*matrix[2][3])
                       / matrix[2][2], 5)
        lst[1] = round((vector[1]-lst[2]*matrix[1][2]-lst[3]*matrix[1][3])
                       / matrix[1][1], 5)
        lst[0] = round((vector[0]-lst[1]*matrix[0][1]-lst[2]*matrix[0][2]-lst[3]*matrix[0][3])
                       / matrix[0][0], 5)
    return lst
