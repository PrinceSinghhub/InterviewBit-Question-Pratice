class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):

        divid = 10000000

        return (A+B) % divid


ans = Solution()
a = 10
b = 5
print(ans.solve(a,b))