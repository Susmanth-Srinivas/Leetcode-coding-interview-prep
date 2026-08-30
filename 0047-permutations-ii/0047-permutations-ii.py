class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(start):
            if start == n:
                result.append(nums[:])
                return

            seen = set()
            for i in range(start,n):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])

                nums[start],nums[i]= nums[i],nums[start]
                backtrack(start+1)
                nums[start],nums[i]= nums[i],nums[start]

        backtrack(0)
        return result
