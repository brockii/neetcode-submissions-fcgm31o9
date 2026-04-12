class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        oldLen = len(nums)
        newLen = len(set(nums))
        return oldLen != newLen