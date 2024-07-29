class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l<= r:
            m = l + ((r - l) // 2)
            if  m**2 > x:
                r = m - 1
            elif  m**2 < x:
                l = m+1
                res = m
            else:
                return m
        return res
# or bruteforce


class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x + 1):
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1
        return x
