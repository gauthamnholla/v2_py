from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        cur = [1 << (ord(ch) - 97) for ch in s]  # current letter bit at each node

        # --- Iterative DFS from root 0: parent, depth, root-to-node masks, preorder ---
        parent = [0] * n
        depth = [0] * n
        base = [0] * n
        base[0] = cur[0]
        seen = [False] * n
        seen[0] = True
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    base[v] = base[u] ^ cur[v]
                    stack.append(v)

        # Subtree of v occupies positions tin[v] .. tout[v] in preorder
        tin = [0] * n
        for i, v in enumerate(order):
            tin[v] = i
        size = [1] * n
        for v in reversed(order):
            if v != 0:
                size[parent[v]] += size[v]
        tout = [tin[v] + size[v] - 1 for v in range(n)]

        # --- Fenwick tree (XOR): range update, point query ---
        bit = [0] * (n + 1)

        def bit_update(i: int, val: int) -> None:
            i += 1
            while i <= n:
                bit[i] ^= val
                i += i & -i

        def bit_query(i: int) -> int:
            i += 1
            res = 0
            while i > 0:
                res ^= bit[i]
                i -= i & -i
            return res

        def path_mask_from_root(v: int) -> int:
            return base[v] ^ bit_query(tin[v])

        # --- Binary lifting for LCA ---
        LOG = max(1, (n - 1).bit_length())
        up = [parent[:]]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[v]] for v in range(n)])

        def lca(a: int, b: int) -> int:
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            k = 0
            while diff:
                if diff & 1:
                    a = up[k][a]
                diff >>= 1
                k += 1
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return parent[a]

        # --- Process queries ---
        answer = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                x = int(parts[1])
                new = 1 << (ord(parts[2]) - 97)
                delta = cur[x] ^ new
                if delta:
                    cur[x] = new
                    bit_update(tin[x], delta)
                    if tout[x] + 1 < n:
                        bit_update(tout[x] + 1, delta)
            else:
                u, v = int(parts[1]), int(parts[2])
                w = lca(u, v)
                mask = path_mask_from_root(u) ^ path_mask_from_root(v) ^ cur[w]
                answer.append(mask & (mask - 1) == 0)  # at most one odd letter

        return answer