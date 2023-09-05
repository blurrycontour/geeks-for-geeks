# https://practice.geeksforgeeks.org/problems/print-adjacency-list-1587115620/1

from typing import List


class Solution:
    def printGraph(self, V : int, edges : List[List[int]]) -> List[List[int]]:
        adj_list = [set() for _ in range(V)]
        for v1,v2 in edges:
            adj_list[v1].add(v2)
            adj_list[v2].add(v1)
        return adj_list


if __name__ == "__main__":
    cases = [
        (5, [(0,1),(0,4),(4,1),(4,3),(1,3),(1,2),(3,2)]),
        (4, [(0,3),(0,2),(2,1)]),
    ]

    for c in cases:
        s = Solution()
        res = s.printGraph(*c)
        for row in res:
            print(*sorted(row))
        print('-'*10)
