class Solution:

    def solve(self, A):

        Max = max(A)
        Min = min(A)

        return Max+Min

ans = Solution()
arr = [2,1,4,5,7,8]
print(ans.solve(arr))