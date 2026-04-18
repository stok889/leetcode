class Solution:
    def reverse(self, x: int) -> int:
        ret = 0
        s = 1
        if x < 0:
            s = -1
            x *= -1

        while x != 0:
            n = x % 10
            ret = ret * 10 + n
            x //= 10

        if ret > (1 << 31) or ret < -1 * (1 << 31):
            ret = 0

        return ret * s
        
if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(120))    
    print(s.reverse(-123))    
    print(s.reverse(1534236469))        