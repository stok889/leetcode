#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        bool ret = true;
        int n = arr.size();
        int m[10000], d[10000];
        
        memset(m, 0, sizeof(m));
        memset(d, 0, sizeof(d));

        for (int i = 0; i < n; ++i) {
            ++m[arr[i] + 1000];
        }

        for (int i = 0; i < 10000; ++i) {
            if (m[i] == 0) continue;
            if (d[m[i]] == 1) {
                ret = false;
                break;
            }
            d[m[i]] = 1;
        }

        return ret;        
    }
};

int main() {
    Solution s;
    vector<int> m({1,2,2,1,1,3});
    bool a = s.uniqueOccurrences(m);
    if (a) printf("true\n");
    else printf("false\n");
    m = {1,2};
    a = s.uniqueOccurrences(m);
    if (a) printf("true\n");
    else printf("false\n");
    m = {-3,0,1,-3,1,1,1,-3,10,0};
    a = s.uniqueOccurrences(m);
    if (a) printf("true\n");
    else printf("false\n");

    return 0;
}
