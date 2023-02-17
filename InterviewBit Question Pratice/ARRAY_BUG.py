class Solution:

    def rotateArray(self, a, b):


        ret = []

        for i in range(len(a)):
            ret.append(a[(i+b)%len(a)])
        return ret

ans = Solution()

A = [ 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35 ]
B = 56
print(ans.rotateArray(A,B))