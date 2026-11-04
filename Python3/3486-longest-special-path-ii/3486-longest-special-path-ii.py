from typing import List

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        last = {}            # value -> depth index of its latest occurrence on the current path
        dist = [0] * n       # dist[d] = distance from root to the node at depth d on the current path
        best_len, best_nodes = 0, 1

        # Stack frames: (node, parent, depth, distance, max1, max2, restore)
        # max1 >= max2 are the two largest "previous occurrence" indices on the path so far
        stack = [(0, -1, 0, 0, -1, -1, None)]
        while stack:
            node, parent, d, dis, m1, m2, restore = stack.pop()
            if node is None:
                # Exit marker: restore the value's previous last occurrence
                val, old = restore
                if old is None:
                    del last[val]
                else:
                    last[val] = old
                continue

            dist[d] = dis
            v = nums[node]
            p = last.get(v, -1)
            # Update the two largest previous-occurrence indices
            if p > m1:
                m1, m2 = p, m1
            elif p > m2:
                m2 = p

            start = m2 + 1   # earliest depth allowed: at most one repeated value in the window
            length = dis - dist[start]
            count = d - start + 1
            if length > best_len or (length == best_len and count < best_nodes):
                best_len, best_nodes = length, count

            stack.append((None, None, None, None, None, None, (v, last.get(v))))
            last[v] = d
            for nxt, w in adj[node]:
                if nxt != parent:
                    stack.append((nxt, node, d + 1, dis + w, m1, m2, None))

        return [best_len, best_nodes]