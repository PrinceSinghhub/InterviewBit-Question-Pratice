import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        a=[]
        def isprime(k):
            i=2
            b=math.sqrt(k)
            while(i<=b):
                if(k%i==0):
                    return 0
                i=i+1
            return 1
        i=2
        while(i<=A/2):
            if(isprime(i) and isprime(A-i)):
                a.append(i)
                a.append(A-i)
                return a
            i=i+1

ans = Solution()
n = 10
print(ans.primesum(n))