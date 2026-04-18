class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0

        for i in range(32):
            ret <<= 1
            if n & 1:
                ret += 1
            n >>= 1

        return ret
        
if __name__ == "__main__":
    s = Solution()
    print(s.reverseBits(43261596))
    print(s.reverseBits(2147483644))