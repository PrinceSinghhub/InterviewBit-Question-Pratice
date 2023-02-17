class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):

        Binary = bin(A)

        return Binary[2::]


ans = Solution()
n = 100
print(ans.findDigitsInBinary(n))