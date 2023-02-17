class Solution:

    def solve(self, A, B, C, D, E):
        m = float('inf')
        for i in range((A // B) + 1):
            if (A - B * i) % D == 0:
                m = min(m, C * i + ((A - B * i) // D) * E)
        if m == float('inf'):
            return -1
        else:
            return m

ans = Solution()
A = 5
B = 3
C = 3
D = 3
E = 2
print(ans.solve(A,B,C,D,E))