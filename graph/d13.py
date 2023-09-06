# https://practice.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1

from typing import List
from collections import deque

class Solution:
    # Using BFS
    def minimumMultiplicationsBFS(self, arr : List[int], start : int, end : int) -> int:
        q = deque([(start, 0)])
        steps = [1e8] * 100000  # visited, step to reach a number
        while q:
            x, step = q.popleft()
            if x == end:
                return step
            for n in arr:
                y = (x*n)%100000
                if step+1 < steps[y]:
                    q.append((y,step+1))
                    steps[y] = step+1
        return -1

    def minimumMultiplicationsDFS(self, arr : List[int], start : int, end : int) -> int:
        stack = [(start, 0)]
        steps = [1e8] * 100000  # visited, step to reach a number
        min_step = 1e8
        found = False
        while stack:
            x, step = stack.pop()
            if x == end and step < min_step:
                found = True
                min_step = step
            for n in arr:
                y = (x*n)%100000
                if step+1 < steps[y]:
                    stack.append((y,step+1))
                    steps[y] = step+1
        return min_step if found else -1


if __name__ == "__main__":
    cases = [
        ([2,5,7], 3, 30), # 2
        ([3,4,65], 7, 66175), # 4
    ]

    for c in cases:
        s = Solution()
        res1 = s.minimumMultiplicationsBFS(*c)
        res2 = s.minimumMultiplicationsDFS(*c)
        print(res1,res2)
