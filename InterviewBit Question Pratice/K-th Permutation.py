class Solution:
    # @param A : integer
    # @param B : long
    # @return a list of integers
    def findPerm(self, A, B):
        fact = [0] * 21
        fact[0] = 1
        for i in range(1, 21):
            fact[i] = i * fact[i - 1]

        ans = [0] * A
        curr = 0
        for i in range(A - 20):
            ans[i] = i + 1
            curr = i

        l1 = []
        for i in range(max(A - 20, 1), A + 1):
            l1.append(i)
        B -= 1

        for i in range(min(20, A - 1), -1, -1):
            idx = (B // fact[i])
            B -= idx * fact[i]
            ans[curr] = l1[idx]
            curr += 1
            l1.pop(idx)

        return ans

ans = Solution()
n =3
m = 3
print(ans.findPerm(n,m))

for i in range(0,10,2):
    print(i)
