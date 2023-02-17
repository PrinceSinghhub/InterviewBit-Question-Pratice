class Solution:
    def maxset(self, A):
        indicies = []
        rs = 0
        rstDic = {}

        for i in range(len(A)):
            if A[i] >= 0:
                rs += A[i]
                indicies.append(A[i])
            else:
                if rs in rstDic:
                    if len(indicies) > len(rstDic[rs]):
                        rstDic[rs] = indicies
                else:
                    rstDic[rs] = indicies

                indicies = []
                rs = 0

        if len(rstDic) == 0 and rs > 0:
            return indicies
        elif len(rstDic) > 0 and max(rstDic) < rs:
            return indicies

        return rstDic[max(rstDic)]

ans = Solution()
A = [1, 2, 5, -7, 2, 3]
print(ans.maxset(A))