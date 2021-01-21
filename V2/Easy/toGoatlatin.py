class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowels = ['a','e','i','o','u']
        i = 1
        result = ""
        S = S.split(' ')
        for s in S:
            if s[0] == ' ':
                continue
            if s[0].lower() in vowels:
                s = s + "ma"
            else:
                s = s[1:] + s[0] + "ma"
            s += 'a' * i
            i += 1
            result += s
            result += ' '
        return result[0:len(result)-1]
            
        