class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)

        sum_real = sum(A)
        sum_square_real = 0

        for x in A:
            sum_square_real += x * x

        A_B = sum_real - (n * (n + 1)) // 2

        A2_B2 = sum_square_real - (n * (n + 1) * (2 * n + 1)) // 6

        A_plus_B = A2_B2 / A_B

        missing = (abs(A_plus_B + A_B)) / 2

        repeat = (abs(A_plus_B - A_B)) / 2

        return [int(missing), int(repeat)]

ans = Solution()
arr = [3,1,2,5,3]
print(ans.repeatedNumber(arr))
