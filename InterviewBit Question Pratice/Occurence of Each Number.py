from collections import Counter


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, A):

        # bruteforce Approch
        # a = list(set(A))
        # a.sort()

        # ans = []

        # for i in a:
        #     ans.append(A.count(i))

        # return ans

        # optimize code

        arr = Counter(A)

        # print(arr)

        val = arr.values()
        key = arr.keys()

        key = list(key)
        key.sort()


        ans = []

        for i in key:
            ans.append(arr[i])

        return ans



ans = Solution()



a = [ 1, 2, 3, 2, 2, 1, 2, 2, 2, 1 ]
print(ans.findOccurences(a))