class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A < 10:
            return A

        A = A % 10 + self.solve(A // 10)
        return self.solve(A)

ans = Solution()
A = 9956782345098712347865490832469987
print(ans.solve(A))
a = {'a':10,'b':20,'u':500}
print(a.get('a'))