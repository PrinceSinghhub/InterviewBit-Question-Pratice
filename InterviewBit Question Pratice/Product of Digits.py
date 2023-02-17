class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        if A == 0:
            return 0


        ans = 1

        while A >= 1:
            mod = A%10
            ans*=mod
            A = A//10
        return ans

ans = Solution()
n = 123
print(ans.solve(n))
