class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index, current):
            # base case: built a combination the same length as digits
            if index == len(digits):
                result.append("".join(current))
                return

            letters = digit_map[digits[index]]
            for letter in letters:
                current.append(letter)         # choose
                backtrack(index + 1, current)  # explore
                current.pop()                  # un-choose (backtrack)

        backtrack(0, [])
        return result