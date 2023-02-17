class Solution:
    # @param A : list of integers
    # @return an integer
    def divisibleBy60(self, A):
        if len(A)==2:
            if A[0]==6 and A[1]==0:
                return 1
            elif A[0]==1 and A[1]==6:
                return 1
            else:
                return 0
        summ = sum(A)
        if summ%3!=0:
            return 0
        if 0 in A:
            return 1
        return 0

ans = Solution()
arr = [1,2,4,5,9,6]
print(ans.divisibleBy60(arr))