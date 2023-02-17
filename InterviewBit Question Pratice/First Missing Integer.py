class Solution:
    def firstMissingPositive(self, A):
        arrayLen = len(A)
        A = set(A)
        for i in range(1, arrayLen + 2):
            if not i in A:
                return i
        return 1

ans = Solution()
arr = [1,2,0]
print(ans.firstMissingPositive(arr))
