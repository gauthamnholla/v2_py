from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        # DFS on the original tree, keeping a stack of ancestors for each letter
        new_parent = parent[:]
        last = [[] for _ in range(26)]   # last[c] = stack of ancestors with letter c
        order = []
        stack = [(0, False)]
        while stack:
            node, leaving = stack.pop()
            c = ord(s[node]) - 97
            if leaving:
                last[c].pop()
                continue
            order.append(node)
            if node and last[c]:
                new_parent[node] = last[c][-1]   # closest ancestor with the same letter
            last[c].append(node)
            stack.append((node, True))
            for ch in children[node]:
                stack.append((ch, False))

        # New parents are original ancestors, so reverse preorder is children-first
        size = [1] * n
        for node in reversed(order):
            if node:
                size[new_parent[node]] += size[node]
        return size