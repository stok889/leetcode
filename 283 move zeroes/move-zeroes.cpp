#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        int i = 0;

        while (i < n) {
            if (nums[i] == 0) {
                int f = 0;
                for (int j = i + 1; j < n; ++j) {
                    if (nums[j] != 0) f = 1;
                    swap(nums[j - 1], nums[j]);
                }
                if (!f) break;
                continue;
            }
            ++i;
        }
    }
};

int main() 
{
    Solution s;
    vector<int> m({0, 1, 0, 3, 5, 12});
    s.moveZeroes(m);
    for (int i = 0; i < m.size(); ++i) printf("%d ", m[i]);
    printf("\n");
    m = {0};
    s.moveZeroes(m);
    for (int i = 0; i < m.size(); ++i) printf("%d ", m[i]);
    printf("\n");
    m = {0, 1, 0};
    s.moveZeroes(m);
    for (int i = 0; i < m.size(); ++i) printf("%d ", m[i]);
    printf("\n");
    m = {0, 1};
    s.moveZeroes(m);
    for (int i = 0; i < m.size(); ++i) printf("%d ", m[i]);
    printf("\n");
    m = {0, 0, 0, 0, 0, 0, 1};
    s.moveZeroes(m);
    for (int i = 0; i < m.size(); ++i) printf("%d ", m[i]);
    printf("\n");

    return 0;
}
