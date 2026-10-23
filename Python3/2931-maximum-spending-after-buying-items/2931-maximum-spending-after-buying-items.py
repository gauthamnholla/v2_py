class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        heap = [(values[i].pop(), i) for i in range(m)]
        heapify(heap)

        res = 0
        for d in range(1, m * n + 1):
            value, idx = heappop(heap)
            res += value * d
            if len(values[idx]) > 0:
                heappush(heap, (values[idx].pop(), idx))
        return res