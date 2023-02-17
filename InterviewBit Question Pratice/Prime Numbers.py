class Solution:
    # @param A : integer
    # @return a list of integers

    def checkprime(self, num):
        ans = True

        check = 2

        while check * check <= num:
            if num % check == 0:
                ans = False
                break
            check += 1
        if ans == True:
            return 1
        return 0

    def sieve(self, A):

        prime = []
        for i in range(2, A + 1):

            ans = self.checkprime(i)
            if ans == 1:
                prime.append(i)

        return prime

ans = Solution()
N = 20
print(ans.sieve(N))