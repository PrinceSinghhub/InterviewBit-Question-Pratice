class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        for i in A:
            if i % B != 0:
                return 0
        return 1

ans = Solution()
A=[2,3,1]
X=1
print(ans.solve(A,X))