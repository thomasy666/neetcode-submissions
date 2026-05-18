class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            complement = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while k > j:
                if k > j and nums[j]+nums[k] < complement:
                    j += 1;
                if k > j and nums[j]+nums[k] > complement:
                    k -= 1;
                if k > j and nums[j]+nums[k] == complement:
                    if (j != i and k != i):
                        res.append([nums[i],nums[j],nums[k]])
                        j += 1
                        k -= 1
                        while nums[j] == nums[j - 1] and j < k:
                            j += 1
                        continue
        return res