# Problem: https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[0] - t[1])

        energy = 0  
        result = 0  

        for actual, minimum in tasks:
            if energy < minimum:
                result += minimum - energy
                energy = minimum
            energy -= actual

        return result