class Solution:
    def minQueenMoves(self, source, target):
        sameX = source[0] == target[0]
        sameY = source[1] == target[1]

        if sameX and sameY: return 0
        if sameX or sameY: return 1
        if abs(source[0] - target[0]) == abs(source[1] - target[1]): return 1
        return 2