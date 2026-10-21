class Solution:
    def checkDistances(self, s: str, distance: list[int]) -> bool:
        a = ord('a')
        for c in s:
            idx1 = s.find(c)
            idx2 = s.find(c,idx1+1)
            if distance[ord(c)-a] != idx2 - idx1 - 1:
                return False
        return True