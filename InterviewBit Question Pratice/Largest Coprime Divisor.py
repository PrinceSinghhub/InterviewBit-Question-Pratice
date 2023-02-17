def gcd(A, B):
    while B:
        A, B = B, A % B
    return A


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def cpFact(self, A, B):
        denom = 2  # dummy value for gcd so the while loop executes
        while denom > 1:
            denom = gcd(A, B)
            A = A / denom
        return A