class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxCount = 1
        for num in nums:
            if num-1 in nums:
                continue
            count = 1
            while (num + count) in nums:
                count += 1
            maxCount = max(count, maxCount)
        return maxCount