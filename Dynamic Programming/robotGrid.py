import pandas as pd


# http://articles.leetcode.com/unique-paths/
# memoization solution not easy bc we need to store ALL possible paths to the destination from EVERY point
def findPaths(mat, r, c, path=None):
    if path == None:
        path = ''
    rDest = len(mat) - 1
    cDest = len(mat[0]) - 1
    if r == rDest and c == cDest:
        print(path)
    if r > rDest or c > cDest or mat[r][c] == 'X':
        return  # current path is useless
    findPaths(mat, r, c + 1, path + 'R')
    findPaths(mat, r + 1, c, path + 'D')


def findPathsDP(mat):
    rDest = len(mat) - 1
    cDest = len(mat[0]) - 1
    dCount, cCount, rowX, colX = 0, 0, False, False
    # setup the outer rows and columns
    for r in range(rDest, -1, -1):
        if mat[r][cDest] == 'X':
            rowX = True
        mat[r][cDest] = 'X' if rowX else ['D' * dCount]
        dCount += 1
    for c in range(cDest, -1, -1):
        if mat[rDest][c] == 'X':
            colX = True
        mat[rDest][c] = 'X' if colX else ['R' * cCount]
        cCount += 1
    # dp begins. start at one diagonal index upwards
    for r in range(rDest - 1, -1, -1):
        for c in range(cDest - 1, -1, -1):
            if mat[r][c] != 'X':
                rightPaths = [] if mat[r][c + 1] == 'X' else list(map(lambda x: 'R' + x, mat[r][c + 1]))
                downPaths = [] if mat[r + 1][c] == 'X' else list(map(lambda x: 'D' + x, mat[r + 1][c]))
                mat[r][c] = rightPaths + downPaths
    print(pd.DataFrame(mat))
    return mat[0][0]


findPaths([[0, 0, 0], [0, 'X', 0], [0, 0, 0]], 0, 0)
print(findPathsDP([['0', '0', '0'], ['0', 'X', '0'], ['0', '0', '0']]))
