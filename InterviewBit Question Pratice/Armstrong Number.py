class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):


        org = A
        ans = 0

        L = len(str(A))

        while A > 0:
            digit = A%10
            Pow = pow(digit,L)
            # print(Pow)
            ans+=Pow
            A = A//10

        # print(org)
        # print(ans)
        if org == ans:
            return 1
        return 0


ans = Solution()
n = 153
print(ans.solve(n))
print(pow(8,4))

