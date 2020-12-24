class Solution:
    def countNumbersWithUniqueDigits(self, n):
        result = 0
        for i in range(0, 10**n):
            num = str(i)
            if len(num) == 1:
                result += 1
            elif self.containsDuplicates(num):
                result += 1
        return result
        
    def containsDuplicates(self, num):
        i = 0
        while i != len(num)-1:
            if num[i] in num[i+1:]:
                return False
            else:
                i += 1
        return True
    
         

s = Solution()
print(s.countNumbersWithUniqueDigits(7))
