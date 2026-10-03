class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):          # used every digit
                    res.append(".".join(parts))
                return

            for length in range(1, 4):       # segment of 1, 2, or 3 digits
                if start + length > len(s):  # not enough digits left
                    break

                seg = s[start:start + length]

                if seg[0] == '0' and length > 1:   # leading zero
                    break
                if int(seg) > 255:                  # too big
                    break

                parts.append(seg)            # choose
                backtrack(start + length, parts)   # explore
                parts.pop()                  # undo

        backtrack(0, [])
        return res
        