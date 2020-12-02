class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_dict = {}
        for x in nums:
            if x in duplicate_dict:
                duplicate_dict[x] += 1
                if duplicate_dict[x] == 2:
                    return True
            else:
                duplicate_dict[x] = 1
        return False