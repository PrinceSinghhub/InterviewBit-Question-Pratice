class Solution:
    # @param A : list of list of integers
    # @return an integer
    def setIntersection(self, A):
        n = len(A)
        A.sort(key=lambda x: x[1])
        res = []
        res.append(A[0][1] - 1)
        res.append(A[0][1])
        for i in range(1, n):
            start = A[i][0]
            end = A[i][1]
            size = len(res)
            last = res[size - 1]
            secondLast = res[size - 2]
            if (start > last):
                res.append(end - 1)
                res.append(end)
            elif (start == last):
                res.append(end)
            elif (start > secondLast):
                res.append(end)
        return len(res)


ans = Solution()
A = [[1, 3], [1, 4], [2, 5], [3, 5]]
print(ans.setIntersection(A))