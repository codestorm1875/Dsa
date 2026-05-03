# Problem: https://leetcode.com/problems/sudoku-solver/
# Time Complexity: O(9^m) 
# Space Complexity: O(m) 

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    bit = 1 << int(board[r][c])
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit
                    
        def solve(idx: int) -> bool:
            if idx == len(empty):
                return True
            
            r, c = empty[idx]
            b = (r // 3) * 3 + c // 3
            
            available = ~(rows[r] | cols[c] | boxes[b])
            for i in range(1, 10):
                bit = 1 << i
                if available & bit:
                    board[r][c] = str(i)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[b] |= bit
                    
                    if solve(idx + 1):
                        return True
                        
                    rows[r] ^= bit
                    cols[c] ^= bit
                    boxes[b] ^= bit
                    
            return False
            
        solve(0)