class Solution:

    def getRow(self, A):

        ans = []

        prev = 1

        ans.append(prev)

        for i in range(1, A + 1):
            curr = (prev * (A - i + 1)) // i
            ans.append(curr)
            prev = curr

        return ans

ans = Solution()
n = 3
print(ans.getRow(n))

