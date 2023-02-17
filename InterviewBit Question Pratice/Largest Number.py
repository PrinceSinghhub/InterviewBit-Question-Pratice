class Solution:
    def largestNumber(self, A):

        extval = []
        ans = ""

        l = len(str(max(A))) + 1

        for i in A:
            temp = str(i) * l

            extval.append((temp[:l:], i))

        extval.sort(reverse=True)

        for i in extval:
            ans += str(i[1])

        if int(ans) == 0:
            return "0"
        return ans


ans = Solution()
arr = [3, 30, 34, 5, 9]
print(ans.largestNumber(arr))