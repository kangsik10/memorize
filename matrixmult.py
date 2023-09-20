def matrixmult (n, A, B):
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n) :
            for k in range(n) :
                for k in range(n):
                    C[i][j] += A[i][k]*B[k][j]
    return C