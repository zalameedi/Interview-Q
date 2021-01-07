class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        for w in words:
            if w in allowed:
                result += 1
            else:
                if self.countHelper(allowed, w):
                    result += 1
        return result
    
    def countHelper(self, allowed, w):
        allowed = list(allowed)
        for char in list(w):
            if char in allowed:
                pass
            else:
                return False
        return True