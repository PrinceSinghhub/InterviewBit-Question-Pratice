class Solution:

    def maxArr(self, A):

        def calculateDiff(i, j, arr):
            return abs(arr[i] - arr[j]) + abs(i - j)

        result = 0
        n = len(A)

        for i in range(0, n):
            for j in range(i, n):

                if (calculateDiff(i, j, A) > result):
                    result = calculateDiff(i, j, A)

        return result

ans = Solution()
A=[1, 3, -1]
print(ans.maxArr(A))