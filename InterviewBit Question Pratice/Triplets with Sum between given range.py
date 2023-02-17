class Solution:
    # @param A : list of strings
    # @return an integer
    def min_max(self,numbers):
        count = 0
        max = second_max = third_max = float('-inf')
        min = second_min = float('+inf')
        for x in numbers:
            count += 1
            if x >= max:
                third_max = second_max
                second_max = max
                max = x
            elif second_max<x<max:
                third_max = second_max
                second_max = x
            if third_max <x<=second_max:
                third_max = x
            if x < second_min:
                if x <= min:
                    min, second_min = x, min
                else:
                    second_min = x
        return min, second_min, max, second_max, third_max, count

    def solve(self, L):
        A = []
        B = []
        C = []
        for i in range(len(L)):
            L[i] = float(L[i])
        for i in L:
            if 0<=i<float(2)/3:
                A.append(i)
            elif float(2)/3<=i<=1:
                B.append(i)
            elif 1<i<2:
                C.append(i)

        min_a, second_min_a, max_a, second_max_a, third_max_a, len_a = self.min_max(A)
        min_b, second_min_b, max_b, second_max_b, third_max_b, len_b = self.min_max(B)
        min_c, second_min_c, max_c, second_max_c, third_max_c, len_c = self.min_max(C)

        if len_a >=3:
            if 1 < max_a + second_max_a + third_max_a < 2: return 1
        if len_a >=2 and len_b>=1:
            if 1 < max_a + second_max_a + min_b < 2: return 1
        if len_a >=2 and len_c>=1:
            if 1 < min_a + second_min_a + min_c < 2: return 1
        if len_a >=1 and len_b>=2:
            if 1 < min_a + min_b + second_min_b < 2: return 1
        if len_a >=1 and len_b>=1 and len_c>=1:
            if 1 < min_a + min_b + min_c < 2: return 1
        return 0

ans = Solution()
arr =  [0.6, 0.7, 0.8, 1.2, 0.4]
print(ans.solve(arr))