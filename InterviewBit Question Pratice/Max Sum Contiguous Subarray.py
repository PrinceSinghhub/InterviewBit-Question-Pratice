class Solution:
    def maxSubArray(self, nums):

        boolen = True
        for i in nums:
            if i < 0:
                pass
            else:
                boolen = False
                break
        if boolen == True:
            return max(nums)

        max_sum = 0
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum = cur_sum + nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum

ans = Solution()
A = [1, 2, 3, 4, -10]
print(ans.maxSubArray(A))