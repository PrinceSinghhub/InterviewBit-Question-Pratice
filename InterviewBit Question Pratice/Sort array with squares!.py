class Solution:

    def solve(self, A):

        myarr = []
        for i in A:
            con = abs(i)
            myarr.append(con*con)
        myarr.sort()
        return myarr

ans = Solution()
arr = [ -855, -847, -747, -708, -701, -667, -666, -618, -609]
print(ans.solve(arr))