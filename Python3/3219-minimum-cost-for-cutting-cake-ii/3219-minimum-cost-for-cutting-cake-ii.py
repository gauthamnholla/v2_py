class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], 
                                          verticalCut: List[int]) -> int:
        
        cuts = [(-x, True) for x in horizontalCut]
        cuts.extend([(-x, False) for x in verticalCut])
        heapify(cuts)

        horCuts, verCuts, ans = 1, 1, 0

        while cuts:

            cost, isHoriz = heappop(cuts)

            if isHoriz:
                ans-= cost * verCuts
                horCuts+= 1

            else:
                ans-= cost * horCuts
                verCuts+= 1
        
        return ans