class Solution:
    def arrayStringsAreEqualHelper(self, words):
        final_str = ""
        for i in words:
            final_str += i
        return final_str
            
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if (Solution.arrayStringsAreEqualHelper(self, word1)) == (Solution.arrayStringsAreEqualHelper(self, word2)):
            return True
        else:
            return False
        
        
        