# Problem: https://leetcode.com/problems/cyclically-rotating-a-grid/
# Time Complexity: O(m * n)
# Space Complexity: O(m + n)

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for l in range(min(m, n) // 2):
            r1, c1, r2, c2 = l, l, m - 1 - l, n - 1 - l
            cells = ([(r1, c) for c in range(c1, c2 + 1)] +
                     [(r, c2) for r in range(r1 + 1, r2 + 1)] +
                     [(r2, c) for c in range(c2 - 1, c1 - 1, -1)] +
                     [(r, c1) for r in range(r2 - 1, r1, -1)])
            vals = [grid[r][c] for r, c in cells]
            rot = k % len(vals)
            for (r, c), v in zip(cells, vals[rot:] + vals[:rot]):
                grid[r][c] = v
        return grid