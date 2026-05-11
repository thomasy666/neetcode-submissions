class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        start = []
        for number in nums:
            if number - 1 not in nums:
                start.append(number)
        count = 1
        maxcount = 1
        for number in start:
            while(number + 1 in nums):
                count+=1
                number+=1
            if count > maxcount:
                maxcount = count
            count = 1
        return maxcount