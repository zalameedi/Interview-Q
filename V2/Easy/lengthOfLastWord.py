class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.isspace():
            return 0
        words = [l for l in s.split(' ') if l != '']
        result = len(words[len(words)-1]) 
        if result == 0:
            return len(words[len(words)-2]) 
        return result
