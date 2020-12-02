class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while len(nums) != 0:
            x = nums.pop()
            if x in nums:
                nums.remove(x)
            else:
                return x
        
        