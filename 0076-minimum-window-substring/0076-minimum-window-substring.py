from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        need = Counter(t)
        required = len(need)  # number of unique chars in t that need required frequency
        formed = 0            # number of unique chars currently meeting required frequency

        left = 0
        best_len = float("inf")
        best_range = (0, 0)

        for right, ch in enumerate(s):
            if ch in need:
                need[ch] -= 1
                if need[ch] == 0:
                    formed += 1

            # Contract window from the left while all characters in t are covered
            while formed == required:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_range = (left, right)

                left_ch = s[left]
                if left_ch in need:
                    if need[left_ch] == 0:
                        formed -= 1
                    need[left_ch] += 1
                left += 1

        if best_len == float("inf"):
            return ""
        start, end = best_range
        return s[start : end + 1]