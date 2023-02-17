class Solution:
    def gcd(self, A, B):

        if A==0:
            return B
        return self.gcd(B%A,A)


ans = Solution()
A=40
B = 10
print(ans.gcd(A,B))


