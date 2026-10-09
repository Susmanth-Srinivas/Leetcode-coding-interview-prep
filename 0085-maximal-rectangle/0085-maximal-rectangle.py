class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        

        
        C = len(matrix[0])
        heights = [0] * (C + 1)          # extra 0 flushes the stack
        best = 0
        for row in matrix:
            for j in range(C):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            stack = [-1]
            for j in range(C + 1):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[j]:
                    h = heights[stack.pop()]
                    best = max(best, h * (j - stack[-1] - 1))
                stack.append(j)
        return best