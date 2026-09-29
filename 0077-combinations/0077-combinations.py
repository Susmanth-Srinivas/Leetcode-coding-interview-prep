class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrack(start,path):
            if len(path) == k:
                res.append(path.copy())

            for num in range(start,n+1):
                path.append(num)
                backtrack(num+1,path)
                path.pop()

        backtrack(1,[])
        return res
        
        