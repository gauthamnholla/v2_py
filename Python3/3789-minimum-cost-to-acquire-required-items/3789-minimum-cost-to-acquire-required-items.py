class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        def total(x: int) -> int:
            return (x * costBoth
                    + max(0, need1 - x) * cost1
                    + max(0, need2 - x) * cost2)

        return min(total(0), total(min(need1, need2)), total(max(need1, need2)))