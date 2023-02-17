# vvvvv imp question
class Solution:

    def spiralOrder(self, A):

        ans = []
        r = len(A)
        c = len(A[0])
        top = 0
        right = c - 1
        bottom = r - 1
        left = 0
        count = 0
        while True:
            for i in range(left, right + 1):
                ans.append(A[top][i])
                count += 1
            top += 1
            if count == r * c:
                break
            for i in range(top, bottom + 1):
                ans.append(A[i][right])
                count += 1
            right -= 1
            if count == r * c:
                break
            for i in range(right, left - 1, -1):
                ans.append(A[bottom][i])
                count += 1
            bottom -= 1
            if count == r * c:
                break
            for i in range(bottom, top - 1, -1):
                ans.append(A[i][left])
                count += 1
            left += 1
            if count == r * c:
                break
        return ans


ans = Solution()
arr =[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]
print(ans.spiralOrder(arr))