"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        newIntervals = sorted(intervals, key = self.getStart)
        # print([(newIntervals[i].start, newIntervals[i].end) for i in range(len(newIntervals))])
        length = len(newIntervals)
        if length <= 1: return True
        for i in range(len(newIntervals) - 1):
            interval = newIntervals[i]
            nextInterval = newIntervals[i + 1]
            if interval.end > nextInterval.start:
                return False
        return True

    def getStart(self, interval):
        return interval.start

