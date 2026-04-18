class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        ret = True

        x = num
        x1 = 0
        while x != 0:
            n = x % 10
            x1 = x1 * 10 + n
            x //= 10

        x = x1
        x2 = 0
        while x != 0:
            n = x % 10
            x2 = x2 * 10 + n
            x //= 10

        if num != x2:
            ret = False

        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.isSameAfterReversals(0))
    print(s.isSameAfterReversals(1200))
    print(s.isSameAfterReversals(12))