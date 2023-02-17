class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
       res = 0
       xcount = 0
       space = 0
       n = A.count('x')
       for x in A:
           if x == 'x':
               if space != 0:
                   res += min(n - xcount, xcount) * space;
                   space = 0
               xcount += 1
           else:
               space += 1
       return res % 10000003