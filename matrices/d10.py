# https://practice.geeksforgeeks.org/problems/replace-os-with-xs0052/1

from collections import deque

class Solution:
    def fill(self, n, m, mat):
        new_mat = [['X' for _ in range(m)] for _ in range(n)]

        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 'O':
                    if i == 0 or i == n-1 or j == 0 or j == m-1:
                        q.append((i,j))

        visited = set(q)

        while len(q) != 0:
            i,j = q.popleft()
            new_mat[i][j] = 'O'
            neighbours = [(max(0,i-1),j), (min(n-1,i+1),j), (i,max(0,j-1)), (i,min(m-1,j+1))]
            for ni, nj in neighbours:
                if mat[ni][nj] == 'O' and (ni,nj) not in visited:
                    q.append((ni,nj))
                    visited.add((ni,nj))    # dont add same to queue again

        return new_mat


if __name__ == "__main__":
    cases = [
        (5,4,[['X','X','X','X'],['X','O','X','X'],['X','O','O','X'],['X','O','X','X'],['X','X','O','O']]),
        (5,4,[['X','O','X','X'],['X','O','X','X'],['X','O','O','X'],['X','O','X','X'],['X','X','O','O']]),
        (5,4,[['X','X','X','X'],['X','O','X','X'],['X','O','O','X'],['X','O','X','X'],['X','X','O','O']]),
        (4,5,[['X','O','X','X','X'],['O','X','X','X','O'],['O','X','X','O','X'],['X','X','X','O','O']]),
        (11,9,[
            ['O', 'X', 'X', 'O', 'O', 'X', 'O', 'X', 'O'],
            ['O', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'O'],
            ['X', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'O'],
            ['X', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'O'],
            ['O', 'O', 'X', 'X', 'X', 'X', 'O', 'O', 'X'],
            ['O', 'X', 'O', 'O', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X', 'X', 'O', 'X', 'O', 'X'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X'],
            ['O', 'O', 'O', 'X', 'X', 'O', 'X', 'X', 'X'],
            ['X', 'X', 'O', 'X', 'O', 'X', 'X', 'X', 'O'],
        ])
    ]

    s = Solution()

    for c in cases:
        ans = s.fill(*c)
        for i in range(c[0]):
            for j in range(c[1]):
                print(c[2][i][j], end = " ")
            print()
        print('-'*10)
        for i in range(c[0]):
            for j in range(c[1]):
                print(ans[i][j], end = " ")
            print()
        print('='*10)