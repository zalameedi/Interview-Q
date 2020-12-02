# 1480. Running Sum of 1d Array

class Solution:
    def runningSumHelper(self, nums, i):
        return sum(nums[:i])
    
    def runningSum(self, nums: List[int]) -> List[int]:
        final_ls = []
        for i in range(0, len(nums)):
            final_ls.append(nums[i] + Solution.runningSumHelper(self, nums, i))
        return final_ls
    
            

# def runningSumHelper(nums, i):
#         return sum(nums[:i])
    
# def runningSum(nums):
#     final_ls = []
#     for i in range(0, len(nums)):
#         final_ls.append(nums[i] + runningSumHelper(nums, i))
#     return final_ls

# x = [3,1,2,10,1]
#print(runningSum(x))