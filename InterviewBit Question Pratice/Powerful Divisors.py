class Solution:
    # @param A : list of integers
    # @return a list of integers
    def powerfulDivisors(self, A):
        maxn = 1
        for i in A:
            maxn = max(maxn, i)

        div = [0] * (maxn + 1)
        for i in range(1, maxn + 1):
            for j in range(i, maxn + 1, i):
                div[j] += 1

        count = [0] * (maxn + 1)
        count[1] = 1
        for i in range(2, maxn + 1):
            x = div[i]
            if (x == (-x & x)):
                count[i] = 1

        for i in range(2, maxn + 1):
            count[i] += count[i - 1]

        ans = [0] * len(A)
        for i in range(len(A)):
            ans[i] = count[A[i]]

        return ans

ans = Solution()
arr = [1,6]
print(ans.powerfulDivisors(arr))