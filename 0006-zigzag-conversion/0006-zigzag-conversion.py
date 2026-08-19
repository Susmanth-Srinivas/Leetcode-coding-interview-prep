class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows
        currentRow = 0
        direction = -1  # will flip to +1 on the first step

        for char in s:
            rows[currentRow] += char
            if currentRow == 0 or currentRow == numRows - 1:
                direction *= -1
            currentRow += direction

        return ''.join(rows)