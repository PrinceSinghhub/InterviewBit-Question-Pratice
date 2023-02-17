class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        flag = 0
        for i in reversed(range(1,len(A))):
            if(A[i] > A[i-1]):
                for x in reversed(range(i,len(A))):
                    if(A[x] > A[i-1]):
                        A = A[:i-1] + A[x] + A[i:x] + A[i-1] + A[x+1:]
                        break
                A = A[:i] + "".join(sorted(A[i:]))
                flag = 1
                break
        if flag == 0:
            return "-1"
        else:
            return A

ans = Solution()
A = "218765"
print(ans.solve(A))