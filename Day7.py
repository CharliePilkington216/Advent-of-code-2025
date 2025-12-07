from functools import lru_cache
import os

global Visited
global Grid

def GetInput():
    with open(os.getcwd() + "\\input.txt") as file:
        grid = [list(x.strip()) for x in file.readlines()]
    return Transpose(grid)

def Transpose(grid):
    new_grid = ["" for _ in range(len(grid[0]))]
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            new_grid[i] += grid[j][i]

    return new_grid

def Explored(x, y, n):
    for i in range(len(Visited[x])):
        if n < Visited[x][i][0]:
            Visited[x].insert(i, [y, n])
            return None
        elif y < Visited[x][i][0] and Visited[x][i][0] <= n <= Visited[x][i][1]:
            Visited[x][i][0] = y
            return None
        elif y < Visited[x][i][0] and Visited[x][i][1] < n:
            Visited[x][i] = [y, n]
            return None
        elif Visited[x][i][0] <= y <= Visited[x][i][1] and Visited[x][i][0] <= n <= Visited[x][i][1]:
            return None
        elif Visited[x][i][0] <= y <= Visited[x][i][1] and Visited[x][i][1] < n:
            Visited[x][i][1] = n
            return None
    Visited[x].append([y,n])

def Seen(x, y, n):
    a = 0
    b = len(Visited[x])
    while b > a:
        m = (a + b) // 2
        if Visited[x][m][0] > n:
            b = m
        elif Visited[x][m][1] < y:
            a = m + 1
        else:
            return True
    return False

def Splits(x, y):
    n = Grid[x][y:].find('^') + y
    if n != y - 1 and not(Seen(x, y, n)):
        a = 0 if x - 1 < 0 else Splits(x - 1, n)
        b = 0 if x + 1 >= len(Grid) else Splits(x + 1, n)
        Explored(x, y, n)
        return 1 + a + b
    return 0

@lru_cache
def Paths(x, y):
    n = Grid[x][y:].find('^') + y
    if n != y - 1:
        a = 0 if x - 1 < 0 else Paths(x - 1, n)
        b = 0 if x + 1 >= len(Grid) else Paths(x + 1, n)
        return a + b
    return 1

def Find():
    for i in range(len(Grid)):
        if Grid[i][0] == 'S':
            return i, 0

def Part1():
    x,y = Find()
    return Splits(x, y)

def Part2():
    x,y = Find()
    return Paths(x, y)

Grid = GetInput()
Visited = [[] for _ in range(len(Grid))]

for line in Grid:
    print(line)

ans = Part1()
print(ans)

ans = Part2()
print(ans)

