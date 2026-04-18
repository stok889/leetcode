class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ret = False

        if n != 0 and not(n & (n - 1)):
            ret = True

        return ret
        
if __name__ == "__main__":
    s = Solution()        
    print(s.isPowerOfTwo(2))
    print(s.isPowerOfTwo(16))
    print(s.isPowerOfTwo(3))