class Solution:
   def solve(self, A):
      ans = []
      for i in range(A+1):


         C = 1
         temp = []
         for j in range(1, i+1):
            temp.append(C)
            C = C * (i - j) // j
            print(C)
         if len(temp)>0:
            ans.append(temp)
      return ans


ans = Solution()
n = 3
print(ans.solve(n))