class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):

        if int(str(A)[::-1]) == A:
            return 1
        return 0

ans = Solution()
a =12423
print(ans.isPalindrome(a))