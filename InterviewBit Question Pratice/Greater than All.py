class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        min1=0
        count=0
        for i in A:
            if(i>min1):
                count+=1
                min1=i
        return count

ans = Solution()
arr = [1]
print(ans.wave(arr))