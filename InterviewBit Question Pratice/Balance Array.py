class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        odd = sum([A[i] for i in range(0, len(A), 2)])
        even = sum([A[i] for i in range(1, len(A), 2)])
        carry_val = 0
        counter = 0

        for ind, value in enumerate(A):
            if ind % 2 == 0:
                odd = odd - value + carry_val
            else:
                even = even - value + carry_val
            if odd == even:
                counter += 1
            carry_val = value
        return counter

ans = Solution()
A = [5, 5, 2, 5, 8]
print(ans.solve(A))