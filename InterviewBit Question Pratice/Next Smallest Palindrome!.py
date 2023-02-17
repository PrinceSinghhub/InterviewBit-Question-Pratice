class Solution:
    def is_palindrome(self, a):
        return a == a[::-1]

    def compare(self, left, right):
        for l, r in zip(left, right):
            if l > r:
                return 1
            elif l < r:
                return -1
            else:
                continue
        return 0

    def add_1(self, x):
        ns = ""
        carry = 1

        for c in reversed(x):
            d, r = divmod(int(c) + carry, 10)
            ns += str(r)
            carry = d
        if carry: ns += str(carry)

        return ns[::-1]

    def handle_odd(self, a):
        n = len(a)
        mid = n // 2
        left = a[:mid]
        right = a[mid + 1:]

        if self.compare(left[::-1], right) == 1:
            return left + a[mid] + left[::-1]
        else:
            left = left + a[mid]
            left = self.add_1(left)

            return left + left[::-1][1:]

    def handle_even(self, a):
        n = len(a)
        mid = n // 2
        left = a[:mid]
        right = a[mid:]

        if self.compare(left[::-1], right) == -1:
            left = self.add_1(left)
            return left + left[::-1]
        else:
            return left + left[::-1]

    def solve(self, a):
        if self.is_palindrome(a): a = self.add_1(a)
        if self.is_palindrome(a): return a

        n = len(a)

        if n & 1:
            return self.handle_odd(a)
        else:
            return self.handle_even(a)

ans = Solution()
A = "23545"

print(ans.solve(A))