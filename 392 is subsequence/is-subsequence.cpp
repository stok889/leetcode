#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        int l1 = t.length();
        int l2 = s.length();
        int p = 0;

        for (int i = 0; i < l1; ++i) {
            if (t[i] == s[p]) {
                ++p;
                if (p == l2) break;
            }
        }

        return p == l2 ? true : false;
    }
};

int main() {
    Solution s;

    bool ans = s.isSubsequence("abc", "ahbgdc");
    if (ans) printf("true");
    else printf("false");

    ans = s.isSubsequence("axc", "ahbgdc");
    if (ans) printf("true");
    else printf("false");

    return 0;
}