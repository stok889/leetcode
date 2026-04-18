#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string removeStars(string s) {
        string ret;
        int n = int(s.length());
        int u = 0;

        for (int i = 0; i < n; ++i) {
            if (s[i] == '*') ret.pop_back();
            else ret.push_back(s[i]);
        }
        
        return ret;
    }
};

int main() {
    Solution s;
    string st = "leet**cod*e";
    printf("%s\n", s.removeStars(st).c_str());
    st = "erase*****";
    printf("%s\n", s.removeStars(st).c_str());
}
