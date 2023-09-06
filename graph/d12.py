# https://practice.geeksforgeeks.org/problems/mother-vertex/1

class Solution:

    def dfs(self, u, adj, visited):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                self.dfs(v, adj, visited)

    def findMotherVertex(self, V, adj):
        visited = [False] * V
        candidate = None  # last visited node
        for u in range(V):
            if not visited[u]:
                self.dfs(u, adj, visited)
                candidate = u
        
        visited = [False]*V
        self.dfs(candidate, adj, visited)
        for node_visited in visited:
            if not node_visited:
                return -1
        return candidate



if __name__ == "__main__":
    cases = [
        (5, [[2,3], [0], [1], [4], []]),   # 0
        (5, [[3, 4], [0], [1], [4], []]),   # 0
        (5, [[2], [0], [1, 3], [4], []]),   # 0
        (3, [[1], [], [1]]),    # -1
    ]

    for c in cases:
        s = Solution()
        res = s.findMotherVertex(*c)
        print(res)
