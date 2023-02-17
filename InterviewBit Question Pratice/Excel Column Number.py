class Solution:
    def titleToNumber(self, columnTitle):

        offset = 0
        N = len(columnTitle)
        for i in range(N):
            offset+=26**i

        ans = 0
        for j in columnTitle:
            ans*=26
            ans+=(ord(j)-ord('A'))
        return ans+offset


ans = Solution()
n = 1
print(ans.titleToNumber(n))