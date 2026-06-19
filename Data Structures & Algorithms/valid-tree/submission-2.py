class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        q = deque()
        q.append((0,-1))
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for neighbor in adj[node]:
                if neighbor in visited and neighbor != parent:
                    return False
                elif neighbor == parent:
                    continue
                else:
                    visited.add(neighbor)
                    q.append((neighbor, node))
        return len(visited) == n
