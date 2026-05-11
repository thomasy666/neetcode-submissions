class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        li = set()
        for number in nums:
            if number in li:
                return True
            else:
                li.add(number)
        return False