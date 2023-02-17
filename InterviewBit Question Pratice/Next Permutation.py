class Solution:
    def nextPermutation(self, a):

        i = len(a) - 2
        while not (i < 0 or a[i] < a[i + 1]):
            i -= 1
        if i < 0:
            sorting = sorted(a)
            return sorting
        j = len(a) - 1
        while not (a[j] > a[i]):
            j -= 1
        a[i], a[j] = a[j], a[i]
        a[i + 1:] = reversed(a[i + 1:])
        return a

ans = Solution()
arr = [99,20]
print(ans.nextPermutation(arr))