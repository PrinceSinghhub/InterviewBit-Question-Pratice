import math
class Solution:

    def solve(self, A):
        row = len(A)
        col = len(A[0])
        dp = [[0 for j in range(col)] for i in range(3)]
        vertex_start = [-1 for j in range(3)]
        vertex_end = [-1 for j in range(3)]
        for j in range(col):
            start_index_rgb = [-1] * 3
            end_index_rgb = [-1] * 3
            for i in range(row):
                if -1 not in start_index_rgb:
                    break
                else:
                    if A[i][j] == 'r' and start_index_rgb[0] == -1:
                        start_index_rgb[0] = i
                    elif A[i][j] == 'g' and start_index_rgb[1] == -1:
                        start_index_rgb[1] = i
                    elif A[i][j] == 'b' and start_index_rgb[2] == -1:
                        start_index_rgb[2] = i
            for i in range(row - 1, -1, -1):
                if -1 not in end_index_rgb:
                    break
                else:
                    if A[i][j] == 'r' and end_index_rgb[0] == -1:
                        end_index_rgb[0] = i
                    elif A[i][j] == 'g' and end_index_rgb[1] == -1:
                        end_index_rgb[1] = i
                    elif A[i][j] == 'b' and end_index_rgb[2] == -1:
                        end_index_rgb[2] = i
            if start_index_rgb[1] == -1 or start_index_rgb[2] == -1:
                dp[0][j] = -1
            else:
                dp[0][j] = max(abs(start_index_rgb[1] - end_index_rgb[2]), abs(start_index_rgb[2] - end_index_rgb[1]))
            if start_index_rgb[0] == -1 or start_index_rgb[2] == -1:
                dp[1][j] = -1
            else:
                dp[1][j] = max(abs(start_index_rgb[0] - end_index_rgb[2]), abs(start_index_rgb[2] - end_index_rgb[0]))
            if start_index_rgb[1] == -1 or start_index_rgb[0] == -1:
                dp[2][j] = -1
            else:
                dp[2][j] = max(abs(start_index_rgb[0] - end_index_rgb[1]), abs(start_index_rgb[1] - end_index_rgb[0]))

        for j in range(col):
            for i in range(row):
                if -1 not in vertex_start:
                    break
                else:
                    if A[i][j] == 'r' and vertex_start[0] == -1:
                        vertex_start[0] = j
                    elif A[i][j] == 'g' and vertex_start[1] == -1:
                        vertex_start[1] = j
                    elif A[i][j] == 'b' and vertex_start[2] == -1:
                        vertex_start[2] = j
        for j in range(col - 1, -1, -1):
            for i in range(row):
                if -1 not in vertex_end:
                    break
                else:
                    if A[i][j] == 'r' and vertex_end[0] == -1:
                        vertex_end[0] = j
                    elif A[i][j] == 'g' and vertex_end[1] == -1:
                        vertex_end[1] = j
                    elif A[i][j] == 'b' and vertex_end[2] == -1:
                        vertex_end[2] = j
        ans = 0
        for j in range(col):
            if dp[0][j] != -1 and vertex_start[0] != -1:
                ans = max(ans, math.ceil(
                    ((dp[0][j] + 1) * (max(abs(j - vertex_start[0]), abs(j - vertex_end[0])) + 1)) / 2.0))
            if dp[1][j] != -1 and vertex_start[1] != -1:
                ans = max(ans, math.ceil(
                    ((dp[1][j] + 1) * (max(abs(j - vertex_start[1]), abs(j - vertex_end[1])) + 1)) / 2.0))
            if dp[2][j] != -1 and vertex_start[2] != -1:
                ans = max(ans, math.ceil(
                    ((dp[2][j] + 1) * (max(abs(j - vertex_start[2]), abs(j - vertex_end[2])) + 1)) / 2.0))
        return int(ans)


ans = Solution()
A = ["rrrrr", "rrrrg", "rrrrr", "bbbbb"]
print(ans.solve(A))