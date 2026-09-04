class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2  # how many elements go on the left side overall

        lo, hi = 0, m

        while lo <= hi:
            i = (lo + hi) // 2       # cut position in nums1
            j = total_left - i       # forced cut position in nums2

            # Boundary values, using -inf/+inf for empty sides
            nums1_left  = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            nums2_left  = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Valid partition found
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                hi = i - 1   # i too big, move left
            else:
                lo = i + 1   # i too small, move right

        raise ValueError("Input arrays are not sorted or invalid input")