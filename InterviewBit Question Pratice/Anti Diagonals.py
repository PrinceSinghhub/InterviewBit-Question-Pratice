class Solution:
    def diagonal(self, A):
        n = len(A)
        B = []
        for s in range(0, n):
            x = []
            for i in range(0, s + 1):
                j = s - i
                x.append(A[i][j])
            B.append(x)

        for s in range(n, 2 * n - 1):
            x = []
            for i in range(s - n + 1, n):
                j = s - i
                x.append(A[i][j])
            B.append(x)
        return B

ans = Solution()
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(ans.diagonal(arr))