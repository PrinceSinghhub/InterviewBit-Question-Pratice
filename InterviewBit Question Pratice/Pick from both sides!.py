class Solution:

    def solve(self, A, B):

        res = sum(A[:B])
        summ = res
        for i in range(B):
            summ = summ-A[B-1-i]
            summ = summ + A[len(A)-1-i]
            res = max(res,summ)
        return res

ans = Solution()
A = [5, -2, 3 , 1, 2]
B = 3
print(ans.solve(A,B))