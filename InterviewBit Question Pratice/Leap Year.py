class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):

        if A % 4 == 0 and A % 100 != 0:
            return 1

        elif A % 400 == 0 and A % 100 == 0:
            return 1
        return 0


ans  =Solution()
n = 2024
print(ans.solve(n))