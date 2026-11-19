class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            num_words = j - i
            num_gaps = num_words - 1
            total_chars = sum(len(words[k]) for k in range(i, j))
            total_spaces = maxWidth - total_chars

            if j == n or num_gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                base_spaces, extra = divmod(total_spaces, num_gaps)
                parts = []
                for k in range(i, j - 1):
                    parts.append(words[k])
                    spaces_here = base_spaces + (1 if (k - i) < extra else 0)
                    parts.append(" " * spaces_here)
                parts.append(words[j - 1])
                line = "".join(parts)

            res.append(line)
            i = j

        return res