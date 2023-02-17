class Solution:
    def solve(self, A):

        Pos = 0
        Neg = 0

        for i in A:
            if i == 0:
                continue
            if i < 0:
                Neg += 1
            else:
                Pos += 1

        return [Pos, Neg]


ans = Solution()
a = [1,2,3,4]
print(ans.solve(a))