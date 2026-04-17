class Solution:
    def countBitsN32(self, n: int) -> List[int]:
        ret = [0 for i in range(n + 1)]

        for i in range(n + 1):
            for j in range(32):
                if i & (1 << j):
                    ret[i] += 1

        return ret

    def countBits(self, n: int) -> List[int]:
        #0 -> 0 -> 0
        #1 -> 1 -> 1
        #2 -> 10 -> 1
        #3 -> 11 -> 2 we can right shift 1 to get 1, and check 3 % 2 = 1, so we have 1 + 1 = 2 ones
        #4 -> 100 -> 1 we can right shift 1 to get 10, and check 4 % 2 = 0, so we have 1 + 0 = 1 ones

        ret = [0 for i in range(n + 1)]

        for i in range(1, n + 1):
            ret[i] = ret[i >> 1]
            if i & 1:
                ret[i] += 1

        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.countBits(2))
    print(s.countBits(5))