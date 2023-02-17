class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        cnt = [0 for i in range(n + 1)]
        for i in A:
            cnt[i] +=1

        ans = [i//2 for i in cnt]
        return sum(ans)






ans = Solution()
A = [ 1, 2, 8, 5, 6, 3, 1, 7, 7, 10, 4, 6, 9, 1, 1, 6, 7, 1, 4, 1, 5, 7, 6, 10, 9, 6, 1, 7, 5, 8, 10, 8, 3, 1, 8, 4, 7, 8, 10, 4, 3, 10, 8, 8, 7, 1, 7, 9, 3, 5, 8, 5, 3, 3, 4, 2, 5, 9, 10, 1, 10, 6, 6, 4, 10, 5, 3, 1, 10, 1, 6, 4, 3, 10, 6, 5, 10, 1, 8, 8, 9, 2, 1, 7, 9, 7, 8, 8, 10, 9, 3, 4, 4, 6, 6, 9, 5, 9, 3, 5 ]
print(ans.solve(A))



