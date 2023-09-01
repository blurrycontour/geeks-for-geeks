# https://practice.geeksforgeeks.org/problems/surround-the-1s2505/1

class Solution:
    def Count(self, matrix):
        # Code here
        rows = len(matrix)
        columns = len(matrix[0])
        _matrix = [[1]*(columns+2)]
        for row in matrix:
            _matrix.append([1]+row+[1])
        _matrix.append([1]*(columns+2))
        
        ones = 0
        for i in range(1,1+rows):
            for j in range(1,1+columns):
                if not _matrix[i][j]:
                    continue
                total = 0
                total += _matrix[i-1][j-1]+_matrix[i-1][j]+_matrix[i-1][j+1]
                total += _matrix[i][j-1]+_matrix[i][j+1]
                total += _matrix[i+1][j-1]+_matrix[i+1][j]+_matrix[i+1][j+1]
                total = 8-total
                if (total % 2) == 0 and total > 0:
                    ones += 1
        return ones
    
if __name__ == "__main__":
    s = Solution()
    print(s.Count([[1,1,0],[0,1,0],[0,0,1]])) # 1
