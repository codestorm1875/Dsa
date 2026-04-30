# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time Complexity: O(N)
# Space Complexity: O(min(N, M))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        char_index_map = {}
        max_length = 0
        left = 0
        
        for right, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= left:
                left = char_index_map[char] + 1

            char_index_map[char] = right
            max_length = max(max_length, right - left + 1)
            
        return max_length