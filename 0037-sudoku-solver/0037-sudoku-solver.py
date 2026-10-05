class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # 1. Initialize trackers with already filled digits and collect empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty_cells.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(index: int) -> bool:
            # Base case: successfully filled every empty cell
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            b = (r // 3) * 3 + (c // 3)

            for digit in "123456789":
                # O(1) validity check
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[b]:
                    # Choose
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[b].add(digit)

                    # Explore next cell
                    if backtrack(index + 1):
                        return True

                    # Undo (Backtrack)
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[b].remove(digit)

            return False

        backtrack(0)