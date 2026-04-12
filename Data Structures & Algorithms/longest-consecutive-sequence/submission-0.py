class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest_sequence = 0
        for i in nums:
            current_sequence = 0
            if i-1 in nums:
                continue
            start = i
            current_sequence += 1
            while start + 1 in nums:
                start += 1
                current_sequence += 1
            longest_sequence = current_sequence if current_sequence > longest_sequence else longest_sequence
        
        return longest_sequence
