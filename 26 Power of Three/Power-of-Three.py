from math import log10

class Solution:
    def isPowerOfThreeLineal(self, n: int) -> bool:
        ret = False
        three = [1 for i in range(10000)]
        for i in range(2, 21):
            three[i] = three[i - 1] * 3
        for i in range(21):
            if n == three[i]:
                ret = True
                break
        return ret
    
    def isPowerOfThree(self, n: int) -> bool:
        ret = False

        if n > 0:
            p = log10(n) / log10(3)
            if abs(p - round(p)) < 1e-10:
                ret = True

        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.isPowerOfThree(3))
    print(s.isPowerOfThree(1162261467))