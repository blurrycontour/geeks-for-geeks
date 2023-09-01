# https://practice.geeksforgeeks.org/problems/make-matrix-beautiful-1587115620/1

class Solution:
    def findMinOpeartion(self, matrix, n):
        row_sums = [0]*n
        col_sums = [0]*n
        max_sum = 0
        for i in range(n):
            row_sums[i] = 0
            for j in range(n):
                row_sums[i] += matrix[i][j]
            col_sums[i] = 0
            for j in range(n):
                col_sums[i] += matrix[j][i]
            max_sum = max(row_sums[i], col_sums[i], max_sum)
       
        ops = 0
        i,j = 0,0
        while sum(row_sums+col_sums) != max_sum*2*n:
            _i,_j = i,j
            if row_sums[i] < col_sums[j]:
                increment = max_sum - col_sums[j]
                _j = j + 1
                if _j == n:
                    _j = n - 1
                    _i = min(i+1, n-1)
            else:
                increment = max_sum - row_sums[i]
                _i = i + 1
                if _i == n:
                    _i = n - 1
                    _j = min(j+1, n-1)
            # print(i,j, f'+{increment}')
            row_sums[i] += increment
            col_sums[j] += increment
            matrix[i][j] += increment
            ops += increment
            i,j = _i,_j
        # print(max_sum, col_sums, row_sums)
        return ops


if __name__ == "__main__":
    s = Solution()
    print(s.findMinOpeartion([[1,2],[3,4]], 2)) # 4
    print(s.findMinOpeartion([[1,2,3],[4,2,3],[3,2,1]], 3)) # 6
