class Solution:

    def isPower(self, A):
        if A == 1:
            return 1

        p = 2
        while (2 ** p <= A):
            pthroot = round(A ** (1.0 / p), 8)
            if int(pthroot) == pthroot:
                return 1
            p += 1
        return 0

ans = Solution()
n = 15
print(ans.isPower(n))