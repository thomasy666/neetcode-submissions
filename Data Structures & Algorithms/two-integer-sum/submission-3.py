class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        difference = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in difference:
                return [difference[complement], i]
            else:
                difference[nums[i]] = i