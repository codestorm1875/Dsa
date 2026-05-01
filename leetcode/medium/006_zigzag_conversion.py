# Problem: https://leetcode.com/problems/zigzag-conversion/
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [''] * numRows
        cur_row = 0
        going_down = False

        for ch in s:
            rows[cur_row] += ch
            
            if cur_row == 0 or cur_row == numRows - 1:
                going_down = not going_down
            cur_row += 1 if going_down else -1

        return ''.join(rows)