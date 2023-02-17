# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @param C : integer
#     # @return an integer
#     def solve(self, A, B, C):
#         count = 0

#         while B >= A:
#             ans = B%10
#             if ans == C:
#                 count+=1
#             B-=1

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return self.get(B, C) - self.get(A - 1, C)

    def get(self, x, c):
        ans = x / 10
        if x % 10 >= c:
            ans = ans + 1
        return int(ans)

#         return count

ans = Solution()
a = 11
b = 111
c = 1
print(ans.solve(a,b,c))