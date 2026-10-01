class Solution:
    def grayCode(self, n: int) -> list[int]:
        res=[0]

        for i in range(n):
            add = 1 << i
            res += [x + add for x in reversed(res)]

        return res
        