#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string ret;
        int n1 = word1.length();
        int n2 = word2.length();

        for (int i = 0; i < min(n1, n2); ++i) {
            ret.push_back(word1[i]);
            ret.push_back(word2[i]);
        }

        if (n1 > n2) ret = ret + word1.substr(n2, n1 - n2);
        else ret = ret + word2.substr(n1, n2 - n1);

        return ret;        
    }
};

int main() {
    Solution s;
    string a("abc"), b("pqr");
    printf("%s\n", s.mergeAlternately(a, b).c_str());
    a = "abceeeee";
    b = "pqr";
    printf("%s\n", s.mergeAlternately(a, b).c_str());
    a = "abc";
    b = "pqreeee";
    printf("%s\n", s.mergeAlternately(a, b).c_str());
}