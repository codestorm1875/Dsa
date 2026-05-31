# Problem: https://leetcode.com/problems/destroying-asteroids/
# Time Complexity: O(nlogn)
# Space Complexity: O(1)

class Solution:
    def asteroidsDestroyed(self, mass, asteroids):
        asteroids.sort()
        if mass >= asteroids[-1]:
            return True
        for a in asteroids:
            if mass < a:
                return False
            mass += a
        return True