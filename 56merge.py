from typing import List


class Solution:


    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        remove = []
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i + 1] = [intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
                remove.append(i)
            i = i + 1
        i = len(remove) - 1
        while i >= 0:
            del intervals[remove[i]]
            i = i - 1

        return intervals







if __name__ == "__main__":
    intervals =  [[1,4],[4,5]]
    s = Solution()
    print(s.merge(intervals))