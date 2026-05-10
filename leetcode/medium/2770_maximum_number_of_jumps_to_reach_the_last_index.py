# Problem: https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        size = len(nums)
        max_jumps = [-1] * size
        max_jumps[0] = 0
        for end in range(1, size):
            for start in range(end):
                if max_jumps[start] != -1 and abs(nums[end] - nums[start]) <= target:
                    max_jumps[end] = max(max_jumps[end], max_jumps[start] + 1)
        return max_jumps[-1]