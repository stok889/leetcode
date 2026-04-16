class Solution:
    def fibArray(self, n: int) -> int:
        ret = [0 for i in range(n + 10)]
        ret[1] = 1
        for i in range(2, n + 1):
            ret[i] = ret[i - 1] + ret[i - 2]

        return ret[n]

    def fib(self, n: int) -> int:
        ret = 0
        x, y = 0, 1

        if n == 1:
            ret = y

        for i in range(2, n + 1):
            ret = x + y
            x, y = y, ret

        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.fib(3))        
    print(s.fib(4))        