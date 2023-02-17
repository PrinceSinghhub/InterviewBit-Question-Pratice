import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):

        index = 1
        ans = []
        while (index * index) < A:
            if A % index == 0:
                ans.append(index)
            index += 1

        sqr = int(math.sqrt(A))

        while sqr >= 1:
            if A % sqr == 0:
                ans.append(A // sqr)
            sqr -= 1

        return ans

        # allf = []
        # for i in range(1,A+1):
        #     if A%i == 0:
        #         allf.append(i)
        # return allf


ans = Solution()
n = 10
print(ans.allFactors(n))