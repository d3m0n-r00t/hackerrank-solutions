def floodfill(i, j, mat):
    if i >= len(mat) or j >= len(mat[0]) or i < 0 or j < 0 or mat[i][j] == -1 or mat[i][j] == 0:
        return 0
    else:
        mat[i][j] = -1
        return 1+floodfill(i,j+1,mat)+floodfill(i,j-1,mat)+floodfill(i+1,j,mat)+floodfill(i-1,j,mat)+floodfill(i+1,j+1,mat)+floodfill(i+1,j-1,mat)+floodfill(i-1,j+1,mat)+floodfill(i-1,j-1,mat)

def connectedCell(matrix):
    mat = matrix.copy()
    res = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res.append(floodfill(i, j, mat))
    return max(res)

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int,input().rstrip().split())))
    result = connectedCell(matrix)
    print(result)