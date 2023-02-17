class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):

        ans = []

        zeros = []

        for i in A:
            if i == 0:
                zeros.append(i)
            else:
                ans.append(i)

        ans+=zeros
        return ans



ans = Solution()
A = [0, 1, 0, 3, 12]
print(ans.solve(A))
