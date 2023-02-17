class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(A)
        ans = 0
        B = B % 2
        for x in A:
            if x % 2 != B:
                ans += C

        return ans