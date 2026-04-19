#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int addMinimum(string word) {
        int ret = 0;
        int u = 0;
        char str[3];
        int n = word.length();

        str[0] = 'a';
        str[1] = 'b';
        str[2] = 'c';
        while (u < n) {
            if (word[u] == str[u % 3]) {
                ++u;
                continue;
            }
            word.insert(word.begin() + u, str[u % 3]);
            ++ret;
            ++u;
            ++n;
        }

        if (n % 3) ret += 3 - n % 3;

        return ret;
    }
};

int main() {
    Solution s;
    printf("%d\n", s.addMinimum("b"));
    printf("%d\n", s.addMinimum("aaa"));
    printf("%d\n", s.addMinimum("abc"));
}
