class Solution:
    # @param A : list of list of strings
    # @return an integer
    def highestScore(self, A):

        count = {}
        marks = {}

        for i in A:
            if i[0] not in count and i[0] not in count:
                count[i[0]] = 1
                marks[i[0]] = int(i[1])

            elif i[0] in count and i[0] in count:
                count[i[0]] += 1
                marks[i[0]] += int(i[1])

        ans = []
        for name, mark in marks.items():
            cut = count.get(name)

            temp = round(mark // cut)
            ans.append(temp)

        return max(ans)

ans = Solution()
A = [["Bob", "80"], ["Bob", "90"], ["Alice", "90"], ["Alice", "10"]]
print(ans.highestScore(A))

