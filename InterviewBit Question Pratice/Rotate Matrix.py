class Solution:

    def rotate(self, A):

        ans = []
        for i in range(len(A)):
            arr = []
            for j in range(len(A[i])):
                arr.append(A[j][i])
            ans.append(arr[::-1])

        return ans




ans = Solution()
arr = [
    [1, 2,3],
    [4,5,6],
    [7,8,9]
]
print(ans.rotate(arr))

