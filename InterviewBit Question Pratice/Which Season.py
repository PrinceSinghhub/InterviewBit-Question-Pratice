class Solution:

    def solve(self, A):

        if A > 12:
            return "Invalid"

        list1 = [3, 4, 5]
        list2 = [6, 7, 8]
        list3 = [9, 10, 11]
        list4 = [12, 1, 2]

        if A in list1:
            return "Spring"

        if A in list2:
            return "Summer"

        if A in list3:
            return "Autumn"

        if A in list4:
            return "Winter"


ans = Solution()
n = 6
print(ans.solve(n))