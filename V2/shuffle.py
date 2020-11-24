class Solution:
    def shuffleHelper(self, nums):
        if len(nums) > 0:
            return nums.pop(0)
        
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        split_ls1 = nums[:n]
        split_ls2 = nums[n:]
        final_ls = []
        while len(split_ls1) != 0 and len(split_ls2) != 0:
            final_ls.append(Solution.shuffleHelper(self, split_ls1))
            final_ls.append(Solution.shuffleHelper(self, split_ls2))
        return final_ls
        