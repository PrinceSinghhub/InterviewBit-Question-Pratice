import math
class Solution:
    # @param A : integer
    # @return an integer
    def product(self, a,b):
        a00 =  (a[0][0]*b[0][0]%1000000007 + a[0][1]*b[1][0]%1000000007)%1000000007
        a01 =  (a[0][0]*b[0][1]%1000000007 + a[0][1]*b[1][1]%1000000007)%1000000007
        a10 =  (a[1][0]*b[0][0]%1000000007 + a[1][1]*b[1][0]%1000000007)%1000000007
        a11 =  (a[1][0]*b[0][1]%1000000007 + a[1][1]*b[1][1]%1000000007)%1000000007
        return ((a00,a01),(a10,a11))
    def rec(self,mat,n):
        if(n==1):
            return mat
        part = self.rec(mat,n//2)
        part = self.product(part,part)
        if(n%2 == 0):
            return part
        return self.product(part,mat)
    def solve(self, A):
        if(A<3):
            return 1
        res = self.rec(((1,1),(1,0)), A-1 )
        return res[0][0]

ans = Solution()
a = 865464656465465
print(ans.solve(a))
