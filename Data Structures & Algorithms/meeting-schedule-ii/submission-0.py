"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)
        start = 0
        end = 0
        count = 0
        res = 0
        while start < len(starts) and end < len(ends):
            if starts[start] < ends[end]:
                count+=1
                start+=1
                res = max(res, count)
            else:
                count-=1
                end+=1
        return res