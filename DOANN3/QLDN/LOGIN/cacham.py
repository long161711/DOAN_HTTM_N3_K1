import numpy as np


def chuyenvi(matrix1, sohang, socot, matrix2):
    for i in range(0, socot,1):
        for j in range(0, sohang, 1):
            matrix2[i][j] = matrix1[j][i]

def nhan2matran(matrix1, matrix2, matrix3, sohang1, socot1, socot2):
    for i in range(0, sohang1,1):
        for j in range(0, socot2,1):
            sum = 0
            for k in range(0, socot1,1):
                sum=(float(matrix1[i][k]) * float(matrix2[k][j]))+sum
            matrix3[i][j]=sum
def tinhdetmatran(matrix, hangcot):
    matrix1 = np.zeros( (hangcot, hangcot) )
    for r in range(0,hangcot, 1):
        for t in range(0, hangcot, 1):
            matrix1[r][t] = matrix[r][t]
    for i in range(0, hangcot-1, 1):
        j = i
        while matrix1[j][i] == 0:
            j = j+1
        if j != i :
            for k in range(0, hangcot, 1):
                A = matrix1[i][k]
                matrix1[i][k] = matrix1[j][k]
                matrix1[j][k] = A
        for p in range (i+1, hangcot, 1):
            if matrix1[p][i] == 0:
                continue
            if matrix1[p][i] != 0:
                m = -matrix1[p][i] / matrix1[i][i]
                for q in range (i, hangcot, 1):
                    matrix1[p][q] = matrix1[p][q] + (matrix1[i][q]*m)
    d = 1
    for w in range(0, hangcot, 1):
        d = d * matrix1[w][w]
    return d


def matranphuhop(matrix, hangcot):
    matrix1 = np.zeros((hangcot, hangcot))
    for r in range(0, hangcot, 1):
        for t in range(0, hangcot, 1):
            matrix1[r][t] = matrix[r][t]
    for i in range(0, hangcot, 1):
        for j in range(0 , hangcot, 1):
            matrix2 = np.zeros((hangcot, hangcot))
            for q in range(0, hangcot-1, 1):
                h = q
                if h >= i:
                    h = h + 1
                for w in range (0, hangcot-1, 1):
                    k = w
                    if k >= j:
                        k = k + 1
                    matrix2[q][w] = matrix1[h][k]
            s = pow((-1), (i+j))
            matrix[i][j] = s * tinhdetmatran(matrix2, hangcot-1)

def matrankhanghic(matrix, hangcot, det):
    for i in range(0, hangcot, 1):
        for j in range(0, hangcot, 1):
            matrix[i][j] = matrix[i][j] * (1/det)
