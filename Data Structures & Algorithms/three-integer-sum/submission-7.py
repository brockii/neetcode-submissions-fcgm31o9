class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        nums_set = set(nums)
        zero_indices = []
        if nums[0] > 0 or nums[-1] < 0:
            return zero_indices

        for i in range(len(nums)-2):
            j = i+1
            if nums[i] + nums[j] > 0 or i > 0 and nums[i-1] == nums[i] : continue
            
            while j < len(nums)-1:
                if -1*(nums[i] + nums[j]) not in nums_set:
                    j += 1
                    continue
                k = j+1
                while k < len(nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        zero_indices.append([nums[i], nums[j], nums[k]])
                    k += 1
                j+=1

        return zero_indices

