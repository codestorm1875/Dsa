# Problem: https://leetcode.com/problems/regular-expression-matching/
# Approach: 
# Time Complexity: O(M * N)
# Space Complexity: O(N)

class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length(), n = p.length();
        vector<bool> prev(n + 1, false), curr(n + 1, false);

        prev[0] = true;
        
        for (int j = 1; j <= n; ++j) {
            if (p[j - 1] == '*') {
                prev[j] = prev[j - 2];
            }
        }

        for (int i = 1; i <= m; ++i) {
            curr[0] = false; 
            for (int j = 1; j <= n; ++j) {
                if (p[j - 1] == '.' || p[j - 1] == s[i - 1]) {
                    curr[j] = prev[j - 1];
                } else if (p[j - 1] == '*') {
                    curr[j] = curr[j - 2] || (prev[j] && (p[j - 2] == '.' || p[j - 2] == s[i - 1]));
                } else {
                    curr[j] = false;
                }
            }
            prev = curr; 
        }

        return prev[n];
    }
};
