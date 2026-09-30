class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        hori = vert = 1
        cuts = [(c, 0) for c in horizontalCut]
        for c in verticalCut: cuts.append((c, 1))
        cuts.sort(reverse=True)
        res = 0
        for c, d in cuts:
            if d == 1:
                res += c * vert
                hori += 1
            else:
                res += c * hori
                vert += 1
        return res