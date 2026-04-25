class Solution:
    def longestPalindrome(self, s: str) -> int:
        ret = 0
        n = len(s)
        d = {}

        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
            
        f = 0
        for x in d.values():
            if x == 1:
                f = 1
                continue
            if x % 2 == 1:
                f = 1
            ret += x // 2
        ret = ret * 2 + f

        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("aa"))
    print(s.longestPalindrome("aab"))
    print(s.longestPalindrome("aabb"))
    print(s.longestPalindrome("ab"))
    print(s.longestPalindrome("aaa"))    