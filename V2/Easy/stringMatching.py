class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = []
        for x in words:
            for y in words:
                if x != y and x in y and x not in substrings:
                    substrings.append(x)
        return substrings