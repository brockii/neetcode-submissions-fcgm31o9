class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first make it a set for easy and faster lookup
        nums_set = set(nums)

        # now iterate through the list with proper checks in place 
        # check 1: The number should be less than target
        # check 2: The other number should be in the set (set won't contain the order)

        # we can also create dictionary for easy lookup + order storing
        for i in range(len(nums)):
            target_indexes = []
            if nums[i] > target:
                continue

            if target - nums[i] not in nums_set:
                continue
            
            j = i + 1 
            
            while j<len(nums) and nums[j] != target - nums[i]:
                j += 1
            target_indexes = [i, j]
            break

        
        return target_indexes

            