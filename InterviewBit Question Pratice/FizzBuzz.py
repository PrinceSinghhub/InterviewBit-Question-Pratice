class Solution:
    # @param A : integer
    # @return a list of strings
    def fizzBuzz(self, A):

        ans = []

        for i in range(1, A + 1):

            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")

            elif i % 3 == 0:
                ans.append("Fizz")

            elif i % 5 == 0:
                ans.append("Buzz")

            else:
                ans.append(str(i))

        return ans


ans = Solution()
n = 15
print(ans.fizzBuzz(n))

