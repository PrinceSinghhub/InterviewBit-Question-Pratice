class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        occupancy = 0
        n = len(arrive)
        if n == 1:
            if K > 0:
                return True
            else:
                return False
        elif n == 0:
            return True
        arrive = sorted(arrive)
        depart = sorted(depart)

        i, j = 0, 0
        while i < n and j < n:
            if arrive[i] < depart[j]:
                occupancy += 1
                if occupancy > K:
                    return False
                i += 1
            else:
                occupancy -= 1
                j += 1

        return True

ans = Solution()
A = [1, 3, 5]
B = [2, 6, 8]
C = 1
print(ans.hotel(A,B,C))