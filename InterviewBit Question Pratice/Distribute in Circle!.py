class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):

        return (C + A % B - 1) % B


ans = Solution()
A = 8
B = 5
C = 2
print(ans.solve(A,B,C))