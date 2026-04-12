class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        for i in nums:
            x[i] = x.get(i, 0) + 1
        frequency_bucket = [[] for i in range(len(nums)+1)]
        
        for key, value in x.items():
            frequency_bucket[value].append(key)

        bucket = []
        for i in range(len(frequency_bucket)-1, 0, -1):
            for j in frequency_bucket[i]:
                bucket.append(j)
                if len(bucket) == k:
                    return bucket