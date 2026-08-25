class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path=[]

        def backtrack(start:int,remaining:int)-> None:
            if remaining == 0:
                result.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,remaining-candidates[i])
                path.pop()

        backtrack(0,target)
        return result
        