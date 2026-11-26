class Solution:
    """
    Understand:
    Input: a list of lists
    Output: a list of merged itervals
    Edge cases: none

    Plan:
    result = []

    for i in range (len(intervals)):
        current = []
        check i[1] with i+1[0], if greater than or equal:
            check minimum of i[0] and i+1[0]
                append minimum to current
                append maximum of i[1] and i+1[1]
        result.append(current)

    return result
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals
        result = []
        intervals.sort(key= lambda first: first[0])
        result.append(intervals[0])

        for i in range(n - 1):
            if result[-1][1] >= intervals[i + 1][0]:
                result[-1][0] = (min(result[-1][0], intervals[i + 1][0]))
                result[-1][1] = (max(result[-1][1], intervals[i + 1][1]))
            else:
                result.append(intervals[i + 1])
        return result
        