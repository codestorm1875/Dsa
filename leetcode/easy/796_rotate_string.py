# Problem: https://leetcode.com/problems/rotate-string/
# Time Complexity: O(n) 
# Space Complexity: O(n) 

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)