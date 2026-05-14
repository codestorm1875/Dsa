# Problem: https://leetcode.com/problems/check-if-array-is-good/
# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)

        if len(nums) != n + 1:
            return False

        nums.sort()

        for i in range(n):
            if nums[i] != i + 1:
                return False

        return nums[n] == n
