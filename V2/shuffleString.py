class Solution:
    def restoreString(self, s, indices):
        temp = list(s)
        final_str = ""
        i = 0
        for x in indices:
            temp[x] = s[i]
            i += 1
            
        final_str = ''.join(str(x) for x in temp)
        return final_str

s = Solution()
print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3]))