from functools import reduce

class Solution:
    def removeDuplicatesStack(self, s: str) -> str:
        ret = []

        for c in s:
            if ret and c == ret[-1]:
                ret.pop()
            else:
                ret.append(c)

        return "".join(ret)

    def removeDuplicates(self, s: str) -> str:
        return reduce(lambda ret, c: ret[:-1] if ret[-1:] == c else ret + c, s)

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates("abbaza"))
    print(s.removeDuplicates("azxxzy"))
    print(s.removeDuplicates("aaaaaa"))
    print(s.removeDuplicates("aaaaaaa"))
    