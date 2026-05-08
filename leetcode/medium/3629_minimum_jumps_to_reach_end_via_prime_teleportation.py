# Problem: https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation/
# Time Complexity: O(n + m) where m = max(nums)
# Space Complexity: O(n + m)

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        V = max(nums) + 1
        spf = list(range(V))
        for i in range(2, int(V**.5) + 1):
            if spf[i] == i:
                for j in range(i * i, V, i):
                    if spf[j] == j: spf[j] = i
        groups = {v: [] for v in set(nums) if v > 1 and spf[v] == v}
        for j, v in enumerate(nums):
            x = v
            while x > 1:
                f = spf[x]
                if f in groups: groups[f].append(j)
                while x % f == 0: x //= f
        dist, q = [-1] * n, [0]; dist[0] = 0
        for i in q:
            for j in [i - 1, i + 1] + groups.pop(nums[i], []):
                if 0 <= j < n and dist[j] < 0:
                    dist[j] = dist[i] + 1
                    if j == n - 1: return dist[j]
                    q.append(j)
        return dist[-1]