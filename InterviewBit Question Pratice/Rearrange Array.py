class Solution:


    def arrange(self, A):
        n = len(A)
        for i in range(n):
            A[i] += (A[A[i]]%n)*n
        for i in range(n):
            A[i] = A[i]//n

        return A


ans = Solution()
arr = [1,0]
print(ans.arrange(arr))