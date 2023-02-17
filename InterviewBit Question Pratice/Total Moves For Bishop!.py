class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        ans = min(A-1,B-1) + min(8-A,B-1)+ min(8-B,A-1) + min(8-A,8-B)

        return ans


ans = Solution()
a = 10
b = 4
print(ans.solve(a,b))