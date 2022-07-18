class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        a = intervals[0][0]
        b = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] > b:
                result.append([a, b])
                a = intervals[i][0]
                b = intervals[i][1]
            elif intervals[i][0] <= b and intervals[i][1] > b:
                b = intervals[i][1]
            else:
                continue
        result.append([a, b])
        return result