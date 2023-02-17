# using function
# import math

# class Solution:
#     # @param A : integer
#     # @param B : integer
#      # @return an long
#     def solve(self, A, B):
#         gcd = math.gcd(A,B)
#         return (A*B)//gcd
class Solution:
    # @param A : integer
    # @param B : integer
     # @return an long
    def hcf(self,a,b):
        if a == 0:
            return b
        return self.hcf(b%a,a)
    def lcm(self,a,b):
        return (a*b)//self.hcf(a,b)

    def solve(self, A, B):

        ans = self.lcm(A,B)
        return ans


ans = Solution()
a = 5
b = 10
print(ans.solve(a,b))