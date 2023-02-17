class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        hours = A[0:2]
        minutes = A[3:]
        count = 0

        while (hours != minutes[::-1]):
            count += 1
            hours = int(hours)
            minutes = int(minutes)
            minutes += 1
            if minutes == 60:
                hours += 1
                minutes = 0
                if hours == 24:
                    hours = 0
            hours = ("0" + str(hours))[-2:]
            minutes = ("0" + str(minutes))[-2:]
        return count

ans = Solution()
A = "23:59"
print(ans.solve(A))