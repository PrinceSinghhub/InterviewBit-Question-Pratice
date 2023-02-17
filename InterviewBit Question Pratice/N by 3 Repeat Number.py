class Solution:

    def repeatedNumber(self, nums):
        nums = list(nums)
        if nums == []:  return -1
        can1, can2, count1, count2 = 0, 1, 0, 0
        for i in nums:
            if i == can1:
                count1 += 1
            elif i == can2:
                count2 += 1
            elif count1 == 0:
                can1, count1 = i, 1
            elif count2 == 0:
                can2, count2 = i, 1
            else:
                count1 -= 1
                count2 -= 1
        if nums.count(can1) > len(nums) / 3: return can1
        if nums.count(can2) > len(nums) / 3: return can2
        return -1

        # bruteforce Approch
        # check = len(A)//3
        # convert = list(set(A))
        # for i in convert:
        #     if A.count(i) > check:
        #         return i

        # return -1

ans = Solution()
arr = [1,2,3,1,1]
print(ans.repeatedNumber(arr))
