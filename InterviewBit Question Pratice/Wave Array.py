class Solution:
    def wave(self, A):
        A = sorted(A)
        for i in range(0, len(A) - 1, 2):
            A[i], A[i + 1] = A[i + 1], A[i]
        return A
ans = Solution()
arr = [ 5, 1, 3, 2, 4 ]
print(ans.wave(arr))


