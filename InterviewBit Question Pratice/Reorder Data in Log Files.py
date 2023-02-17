class Solution:
    # @param A : list of strings
    # @return a list of strings
    def reorderLogs(self, A):
        dig = []
        let = []
        idx_flag = 0
        idx = 0
        for i in range(len(A[0])):
            if idx_flag == 0:
                if A[0][i] == '-' or A[0][i] == "-":
                    idx_flag = 1
                    idx = i
                    break

        for x in A:
            if x[-1] >= 'a' and x[-1] <= 'z':
                temp = x[idx + 1:]
                let.append((x, temp))

            else:
                dig.append(x)

        let.sort(key=lambda x: x[1])
        let = [x for x, y in let]

        return let + dig

ans = Solution()
A = ["dig1-8-1-5-1", "let1-art-can", "dig2-3-6", "let2-own-kit-dig", "let3-art-zero"]
print(ans.reorderLogs(A))