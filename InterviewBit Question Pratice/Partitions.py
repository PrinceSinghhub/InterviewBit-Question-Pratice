class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        total=sum(B)
        if total%3==0:
            target=total//3
        else:
            return 0
        ans=0
        left=0
        right=0
        for i in range(A-1):
            right+=B[i]
            if right==2*target:
                ans+=left
            if right==target:
                left+=1
        return ans

ans = Solution()
A = 5
B = [1, 2, 3, 0, 3]
print(ans.solve(A,B))