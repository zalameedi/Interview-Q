class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = 1
        if (len(strs) == 0):
            return ""
        if (len(strs) == 1):
            return strs[0]
        word = strs[0]
        if word == "":
            return ""
        while True and count != len(word)+1:
            for s in strs:
                if word[0:count] not in s[0:count]:
                    return word[0:count-1]
            count += 1
        return word[0:count]