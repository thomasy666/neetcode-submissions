class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        li = []
        for number in nums:
            if number in li:
                return True
            else:
                li.append(number)
        return False