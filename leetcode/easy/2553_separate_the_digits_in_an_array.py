# Problem: https://leetcode.com/problems/separate-the-digits-in-an-array/
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [b - 48 for b in ''.join(map(str, nums)).encode()]git 