from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        k = len(words)
        need = Counter(words)
        res = []

        for offset in range(word_len):
            left = offset
            seen = Counter()
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                piece = s[right:right + word_len]

                if piece in need:
                    seen[piece] += 1
                    count += 1

                    # too many of this word: shrink from the left
                    while seen[piece] > need[piece]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len

                    # full match: save it, then drop the leftmost word
                    if count == k:
                        res.append(left)
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                else:
                    # not a word: reset the window past this piece
                    seen.clear()
                    count = 0
                    left = right + word_len

        return res