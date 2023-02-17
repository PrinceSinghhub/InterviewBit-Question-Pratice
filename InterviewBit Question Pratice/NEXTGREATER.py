class Solution:
    # @param A : list of integers
    # @return a list of integers

    def find(self, arr, val):

        for i in arr:
            if i > val:
                return i
        return -1

    def nextGreater(self, A):

        ans = []

        for i in range(len(A)):
            v = self.find(A[i + 1::], A[i])
            ans.append(v)
        return ans


