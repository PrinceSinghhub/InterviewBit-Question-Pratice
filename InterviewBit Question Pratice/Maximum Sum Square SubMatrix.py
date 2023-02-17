class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = -float('inf')
        #print(B)
        #print(len(A[0])-B)
        for i in range(0,len(A[0])-B+1):
            s = 0
            for j in range(0, B):
                #print(A[j][i:i+B])
                s += sum(A[j][i:i+B])
            #print(s)
            ans = max(ans,s)
            for k in range(B,len(A)):
                s += -sum(A[k-B][i:i+B])+sum(A[k][i:i+B])
                #print('s',s)
                ans = max(ans,s)
        return ans

ans = Solution()
A = [
        [1, 1, 1, 1, 1]
        [2, 2, 2, 2, 2]
        [3, 8, 6, 7, 3]
        [4, 4, 4, 4, 4]
        [5, 5, 5, 5, 5]
     ]
B = 3
print(ans.solve(A,B))
