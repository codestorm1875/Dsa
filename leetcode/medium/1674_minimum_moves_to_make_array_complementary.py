# Problem: https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
# Time Complexity: O(n + limit)
# Space Complexity: O(limit)

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            lo, hi = min(a, b), max(a, b)
            s = a + b  

            delta[2] += 2
            delta[2 * limit + 1] -= 2

            delta[lo + 1] -= 1
            delta[hi + limit + 1] += 1

            delta[s] -= 1
            delta[s + 1] += 1

        result = n  
        current = 0
        for t in range(2, 2 * limit + 1):
            current += delta[t]
            if current < result:
                result = current

        return result