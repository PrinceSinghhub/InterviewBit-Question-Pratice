class Solution:
    def isPrime(self, A):
        if A == 1:
            return 0
        count = 2
        ans = 0
        while (count*count) <= A:
            if A%count == 0:
                ans+=1
                break
            count+=1

        if ans == 0:
            return 1
        return 0
ans = Solution()
A = 17
print(ans.isPrime(A))

