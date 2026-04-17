class Solution:
    def hammingWeight32(self, n: int) -> int:
        ret = 0

        for i in range(32):
            if n & (1 << i):
                ret += 1

        return ret

    def hammingWeight(self, n: int) -> int:
        ret = 0

        while n > 0:
            if n & 1:
                ret += 1
            n >>= 1

        return ret