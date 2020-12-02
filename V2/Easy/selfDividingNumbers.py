class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        sdn_list = []
        isDividing = False
        for x in range(left, right+1):
            seperate = [int(d) for d in str(x)]
            if(0 not in seperate):
                isDividing = self.selfDividingNumbersHelper(x, seperate)
                if (isDividing == True):
                    sdn_list.append(x)
        return sdn_list
    
    def selfDividingNumbersHelper(self, x, seperate):
        isDividing = False
        for y in seperate:
                if (x % y == 0):
                    isDividing = True
                    continue
                else:
                    isDividing = False
                    return isDividing
        return isDividing
            
                
                
            
                
        