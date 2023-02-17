class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):

        coo = len(A) // 2

        for i in A:
            if A.count(i) > coo:
                return i

        return -1

ans = Solution()
arr = [2, 1, 2]
print(ans.majorityElement(arr))