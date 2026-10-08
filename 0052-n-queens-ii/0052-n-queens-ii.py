class Solution:
    def totalNQueens(self, n: int) -> int:
        cols,diag,anti = set(),set(),set()
        
        def backtrack(r):
            if r == n :
                return 1
            total = 0
            for c in range(n):
                if c in cols or (r-c) in diag or (r+c) in anti :
                    continue
                cols.add(c);diag.add(r-c);anti.add(r+c)
                total += backtrack(r+1)
                cols.remove(c);diag.remove(r-c);anti.remove(r+c)
            return total
        return backtrack(0)

        