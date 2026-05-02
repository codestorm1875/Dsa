# Problem: https://leetcode.com/problems/rotated-digits/
# Time Complexity: O(log n)
# Space Complexity: O(log n)

class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        
        def dp(i: int, is_less: bool, has_diff: bool) -> int:
            if i == len(s):
                return 1 if has_diff else 0
                
            ans = 0
            limit = 9 if is_less else int(s[i])
            
            for d in range(limit + 1):
                if d in (3, 4, 7): 
                    continue
                ans += dp(i + 1, is_less or d < limit, has_diff or d in (2, 5, 6, 9))
                
            return ans
            
        return dp(0, False, False)