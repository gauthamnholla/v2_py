from typing import List

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        n = len(tiles)
        ans = 0
        covered = 0  # white tiles in segments i..j-1, which fit fully under the carpet
        j = 0

        for i in range(n):
            start = tiles[i][0]
            end = start + carpetLen - 1

            # Take in every segment that fits entirely under the carpet
            while j < n and tiles[j][1] <= end:
                covered += tiles[j][1] - tiles[j][0] + 1
                j += 1

            # The next segment may be partly covered
            partial = 0
            if j < n:
                partial = max(0, end - tiles[j][0] + 1)

            ans = max(ans, covered + partial)

            # Slide the window: drop segment i before moving on
            if j > i:
                covered -= tiles[i][1] - tiles[i][0] + 1
            else:
                j = i + 1  # segment i was longer than the carpet; covered stays 0

        return ans