#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> ret;
        int n1 = nums1.size(), n2 = nums2.size();
        int s1[10000], s2[100000];

        memset(s1, 0, sizeof(s1));
        memset(s2, 0, sizeof(s2));

        for (int i = 0; i < n1; ++i)
            s1[nums1[i] + 1000] = 1;
        for (int i = 0; i < n2; ++i)
            s2[nums2[i] + 1000] = 1;

        vector<int> ans;
        for (int i = 0; i < n1; ++i) {
            if (s2[nums1[i] + 1000] == 1) continue;
            s2[nums1[i] + 1000] = 1;
            ans.push_back(nums1[i]);
        }
        ret.push_back(ans);
        ans = {};
        for (int i = 0; i < n2; ++i) {
            if (s1[nums2[i] + 1000] == 1) continue;
            s1[nums2[i] + 1000] = 1;
            ans.push_back(nums2[i]);
        }
        ret.push_back(ans);

        return ret;
    }
};

int main() {
    Solution s;
    vector<int> m1({1, 2, 3}), m2({2, 4, 6});
    vector<vector<int> > ans = s.findDifference(m1, m2);
    for (int i = 0; i < 2; ++i) {
        int n = ans[i].size();
        for (int j = 0; j < n; ++j) {
            printf("%d ", ans[i][j]);
        }
        printf("\n");
    }

    m1 = {};
    m2 = {};
    m1 = {1,2,3,3};
    m2 = {1,1,2,2};
    ans = s.findDifference(m1, m2);
    for (int i = 0; i < 2; ++i) {
        int n = ans[i].size();
        for (int j = 0; j < n; ++j) {
            printf("%d ", ans[i][j]);
        }
        printf("\n");
    }

    return 0;
}