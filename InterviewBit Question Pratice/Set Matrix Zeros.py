class Solution:

    def setZeroes(self, A):

        rowIndex = set()
        collomIndex = set()

        for i in range(len(A)):
            for j in range(len(A[0])):
                if (A[i][j] == 0):
                    rowIndex.add(i)
                    collomIndex.add(j)

        print(rowIndex)
        print(collomIndex)

        for i in rowIndex:
            for e in range(len(A[0])):
                A[i][e] = 0

        for j in collomIndex:
            for e in range(len(A)):
                A[e][j] = 0

        return A



ans  = Solution()
arr =  [[1, 0, 1],
        [1, 1, 1],
        [1, 1, 1]]
print(ans.setZeroes(arr))