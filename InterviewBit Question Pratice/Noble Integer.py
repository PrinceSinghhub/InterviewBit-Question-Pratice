class Solution:
    def solve(self, A):
        A.sort()

        if A[len(A) - 1] == 0:
            return 1

        for i in range(len(A) - 1):
            if A[i] != A[i + 1]:
                count = len(A) - i - 1
                if count == A[i]:
                    return 1
        return -1

ans = Solution()
A = [3, 2, 1, 3]
print(ans.solve(A))