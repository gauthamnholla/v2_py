class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        up_time = [0] * 2001
        tasks.sort(key=lambda t: t[1])
        for task in tasks:
            start, end, duration = task
            duration -= sum(up_time[start:end + 1])
            if duration <= 0:
                continue
            for t in range(end, start - 1, -1):
                if up_time[t] == 1:
                    continue
                up_time[t] = 1
                duration -= 1
                if duration == 0:
                    break
        return sum(up_time)