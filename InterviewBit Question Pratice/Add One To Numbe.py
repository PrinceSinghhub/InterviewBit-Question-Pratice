class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        ans = ""
        for i in A:
            ans += str(i)

        ans = str(int(ans) + 1)
        final_ans = []

        for i in ans:
            final_ans.append(int(i))

        return final_ans


ans = Solution()
arr = [0]
print(ans.plusOne(arr))