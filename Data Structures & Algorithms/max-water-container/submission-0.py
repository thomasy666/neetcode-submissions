class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = -1
        while l < r:
            currArea = (r - l) * min(heights[l], heights[r])
            area = max(currArea, area)
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        return area