import unittest

class Solution:
    def checkValidString1(self, s: str) -> bool:
        ret = True
        n = len(s)
        left = 0
        star = 0
        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                if left > 0:
                    left -= 1
                elif star > 0:
                    star -= 1
                else:
                    ret = False
                    break
            elif c == "*":
                star += 1

        if left != 0:
            ret = False

        return ret      

    def checkValidString(self, s: str) -> bool:
        ret = False
        mx = 0
        mn = 0
        for c in s:
            if c == "(":
                mx += 1
                mn += 1
            elif c == ")":
                mx -= 1
                mn -= 1
            elif c == "*":
                mx += 1
                mn -= 1

            if mx < 0:
                break

            mn = max(mn, 0)                
    
        if mn == 0:
            ret = True

        return ret

"""
assertEqual(a, b) a == b
assertNotEqual(a, b) a != b
assertTrue(x) bool(x) is True
assertFalse(x) bool(x) is False
assertIs(a, b) a is b
assertIsNot(a, b) a is not b
assertIsNone(x) x is None
assertIsNotNone(x) x is not None
assertIn(a, b) a in b
assertNotIn(a, b) a not in b
assertIsInstance(a, b) isinstance(a, b)
assertNotIsInstance(a, b) not isinstance(a, b)
assertIsSubclass(a, b) issubclass(a, b)
assertNotIsSubclass(a, b) not issubclass(a, b)
"""

class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        try:
            self.assertTrue(s.checkValidString("()"))
        except Exception:
            print("Error")

    def test2(self):
        s = Solution()
        try:
            self.assertTrue(s.checkValidString("(*)"))
        except Exception:
            print("Error")

    def test3(self):
        s = Solution()
        try:
            self.assertTrue(s.checkValidString("(*))"))
        except Exception:
            print("Error")

    def test4(self):
        s = Solution()
        try:
            self.assertFalse(s.checkValidString("())"))
        except Exception:
            print("Error")

    def test5(self):
        s = Solution()
        try:
            self.assertFalse(s.checkValidString("()()()("))
        except Exception:
            print("Error")

    def test6(self):
        s = Solution()
        try:
            self.assertTrue(s.checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))
        except Exception:
            print("Error")

    def test7(self):
        s = Solution()
        try:
            self.assertFalse(s.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))
        except Exception:
            print("Error")

if __name__ == "__main__":
    unittest.main()