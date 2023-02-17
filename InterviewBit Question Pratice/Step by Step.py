import math


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # Handling negatives by symmetry
        target = abs(A)

        # Keep moving while sum is smaller i.e calculating n
        n = math.ceil((-1.0 + math.sqrt(1 + 8.0 * target)) / 2)
        sm = (n * (n + 1)) / 2
        n = int(n)
        if (sm == target):
            return n

        d = sm - target

        # case 1 : d is even
        if ((d % 2) == 0):
            return n

        # d is odd
        else:
            if ((n % 2) == 1):
                return n + 2
            else:
                return n + 1

ans = Solution()
n = 15
print(ans.solve(n))