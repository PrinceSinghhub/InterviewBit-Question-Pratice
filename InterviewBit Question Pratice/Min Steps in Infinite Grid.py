class Solution:

	def coverPoints(self, A, B):
		step = 0
		x = 0
		y = 0

		for i in range(1,len(B)):
			x = abs(A[i]-A[i-1])
			y = abs(B[i]-B[i-1])

			step+=min(x,y)
			step+=abs(x-y)
		return step


ans = Solution()
A = [0, 1, 1]
B = [0, 1, 2]

print(ans.coverPoints(A,B))
