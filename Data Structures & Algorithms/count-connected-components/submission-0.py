class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(curr):
            for neighbor in adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components+=1
        return components