import os

def GetInput():
    with open(os.getcwd() + "/input.txt") as file:
        grid = list([list(map(int, [0] + list(x.strip().replace('@', '1').replace('.','0')) + [0])) for x in file.readlines()])
    buffer = [0 for _ in range(len(grid[0]))]
    return [buffer] + grid + [buffer]

def Part1(grid):
    total = 0
    m = len(grid) - 2
    n = len(grid[0]) - 2
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if grid[i][j] == 1 and grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + grid[i][j - 1] + grid[i][j + 1] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1] < 4:
                total += 1
    return total

def Part2(grid):
    total = 0
    m = len(grid) - 2
    n = len(grid[0]) - 2
    add = 1
    while add > 0:
        add = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i][j] == 1 and grid[i - 1][j - 1] + grid[i - 1][j] + grid[i - 1][j + 1] + grid[i][j - 1] + grid[i][j + 1] + grid[i + 1][j - 1] + grid[i + 1][j] + grid[i + 1][j + 1] < 4:
                    add += 1
                    grid[i][j] = 0
        total += add
    return total
        

data = GetInput()

ans = Part1(data)
print(ans)

ans = Part2(data)
print(ans)
