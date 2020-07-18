#Reference : https://www.techiedelight.com/find-longest-possible-route-matrix/

# check if it is possible to go to position (x, y) from
# current position. The function returns false if the cell
# has value 0 or it is already visited.
def isSafe(mat, visited, x, y):
    return not (mat[x][y] == 0 or visited[x][y])


# if not a valid position, return false
def isValid(x, y):
    return M > x >= 0 and N > y >= 0


# Find Longest Possible Route in a Matrix mat from source
# cell (0, 0) to destination cell (x, y)
# 'max_dist' stores length of longest path from source to
# destination found so far and 'dist' maintains length of path from
# source cell to the current cell (i, j)
def findLongestPath(mat, visited, i, j, x, y, max_dist, dist):

    # if destination not possible from current cell
    if mat[i][j] == 0:
        return 0

    # if destination is found, update max_dist
    if i == x and j == y:
        return max(dist, max_dist)

    # set (i, j) cell as visited
    visited[i][j] = 1

    # go to bottom cell
    if isValid(i + 1, j) and isSafe(mat, visited, i + 1, j):
        max_dist = findLongestPath(mat, visited, i + 1, j, x, y, max_dist, dist + 1)

    # go to right cell
    if isValid(i, j + 1) and isSafe(mat, visited, i, j + 1):
        max_dist = findLongestPath(mat, visited, i, j + 1, x, y, max_dist, dist + 1)

    # go to top cell
    if isValid(i - 1, j) and isSafe(mat, visited, i - 1, j):
        max_dist = findLongestPath(mat, visited, i - 1, j, x, y, max_dist, dist + 1)

    # go to left cell
    if isValid(i, j - 1) and isSafe(mat, visited, i, j - 1):
        max_dist = findLongestPath(mat, visited, i, j - 1, x, y, max_dist, dist + 1)

    # Backtrack - Remove (i, j) from visited matrix
    visited[i][j] = 0

    return max_dist


M, N = map(int, input().split())
mat = [[1]*N for i in range(M)]
for _ in range(int(input())):
    x,y = map(int, input().split())
    mat[x][y] = 0
a, b =  map(int, input().split())
x, y = map(int, input().split())
# construct a matrix to keep track of visited cells
visited = [[0 for x in range(N)] for y in range(M)]

# a,b source
#x, y destination
#0,0 = max_dist, dist
max_dist = findLongestPath(mat, visited, a, b, x, y, 0, 0)

print(max_dist)
