class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]  # starting guess

        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # update closest if this sum is nearer to target
                if abs(total - target) < abs(closest - target):
                    closest = total

                if total == target:
                    return total  # can't get any closer than exact
                elif total < target:
                    left += 1   # sum too small, move left up to increase it
                else:
                    right -= 1  # sum too big, move right down to decrease it

        return closest