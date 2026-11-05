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

        # Frames: (node, parent, depth, distance, top) where top = first allowed depth
        # An exit frame has node = None and carries (value, old last index) to restore
        stack = [(0, -1, 0, 0, 0)]
        while stack:
            node, parent, d, dis, top = stack.pop()
            if node is None:
                val, old = parent
                if old is None:
                    del last[val]
                else:
                    last[val] = old
                continue

            dist[d] = dis
            v = nums[node]
            p = last.get(v, -1)
            top = max(top, p + 1)        # window can't include the earlier copy of v

            length = dis - dist[top]
            count = d - top + 1
            if length > best_len or (length == best_len and count < best_nodes):
                best_len, best_nodes = length, count

            stack.append((None, (v, last.get(v)), 0, 0, 0))
            last[v] = d
            for nxt, w in adj[node]:
                if nxt != parent:
                    stack.append((nxt, node, d + 1, dis + w, top))

        return [best_len, best_nodes]