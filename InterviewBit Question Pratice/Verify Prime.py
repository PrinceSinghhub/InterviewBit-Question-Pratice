class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):

        if A == 1:
            return 0

        check = 2
        ans = True
        while check*check <= A:
            if A%check == 0:
                ans = False
                break
            check+=1
        if ans == True:
            return 1
        return 0


ans = Solution()
N = 71
print(ans.isPrime(N))