class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1=set(nums)
        if len(set1)!=len(nums):
            return True
        else:
            return False