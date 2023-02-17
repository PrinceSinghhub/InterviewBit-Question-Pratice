class Solution:

    def solve(self, A):
        n = len(A)
        md = 10 ** 9 + 7

        return ((2 ** n) - 1) % md

ans = Solution()
A = [1, 3]
print(ans.solve(A))