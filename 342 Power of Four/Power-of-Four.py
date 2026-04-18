from math import log10

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        ret = False

        if n > 0:
            p = log10(n) / log10(4)
            if abs(p - round(p)) < 1e-10:
                ret = True

        return ret
