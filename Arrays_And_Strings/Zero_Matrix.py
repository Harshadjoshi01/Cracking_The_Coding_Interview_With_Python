'''
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
Hints: #17, #74, #102

'''

def Zero_Matrix(matrix, m, n):
    row_index = []
    column_index = []
    for i in range(m):
        for j in range(n):
            if (matrix[i][j] == 0 ):
                row_index.append(i)
                column_index.append(j)

    for row in row_index:
        for c in range(n):
            matrix[row][c] = 0
    
    for col in column_index:
        for r in range(m):
            matrix[r][col] = 0
    
    return matrix



if __name__ == '__main__':
    answer = Zero_Matrix([[1,2,0],[0,4,5], [2,3,3]], 3, 3)
    print(answer)