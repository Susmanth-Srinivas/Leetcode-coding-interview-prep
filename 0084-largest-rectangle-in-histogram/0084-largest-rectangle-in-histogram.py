class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights = heights + [0]
        stack = [-1]
        best = 0
        for j,h in enumerate(heights):
            while stack[-1]!= -1 and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = j - stack[-1] - 1
                best = max(best,height* width)
            stack.append(j)
        return best