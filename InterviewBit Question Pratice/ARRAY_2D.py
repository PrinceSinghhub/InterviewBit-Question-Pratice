# /**
# Lets say performOps was called with A : [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# **/
#
# Output:
# 4 3 2 1 8 7 6 5 12 11 10 9
def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in range(len(A)):
        B.append([0] * n)
        for j in range(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B
A =  [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(performOps(A))


