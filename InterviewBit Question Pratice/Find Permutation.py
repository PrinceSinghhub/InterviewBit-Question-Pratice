class Solution:
    def findPerm(self, A, B):
        mn, mx = 1, B
        result = []
        for x in A:
            if x == 'D':
                result.append(mx)
                mx -= 1
            elif x == 'I':
                result.append(mn)
                mn += 1
        result.append(mn)
        return result

ans  = Solution()
n = 3

s = "DI"
print(ans.findPerm(s,n))