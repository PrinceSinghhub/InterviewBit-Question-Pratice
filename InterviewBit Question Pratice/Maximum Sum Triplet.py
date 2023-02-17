class Solution:
    def solve(self, A):

        ans = 0
        n = len(A)

        for i in range(1, (n - 1)):
            max1 = 0
            max2 = 0

            for j in range(0, i):
                if A[j] < A[i]:
                    max1 = max(max1, A[j])

            for j in range((i + 1), n):
                if A[j] > A[i]:
                    max2 = max(max2, A[j])

                    # store maximum answer
                    if (max1 > 0 and max2 > 0):
                        ans = max(ans, max1 + A[i] + max2)

        return ans

ans = Solution()
A = [2, 5, 3, 1, 4, 9]
print(ans.solve(A))
