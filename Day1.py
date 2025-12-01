import os

def GetInput():
    with open(os.getcwd() + "\\input.txt") as file:
        return list([x.strip() for x in file.readlines()])

def Part1(data):
    c = 0
    n = 50
    for line in data:
        l = int(line[1:])

        if line[0] == 'R':
            n = (n + (l % 100)) % 100
        else:
            n = (n - (l % 100)) % 100

        if n == 0:
            c += 1

    return c

def Part2(data):
    c = 0
    n = 50
    for line in data:
        l = int(line[1:])

        if line[0] == 'R':
            c += (n + l) // 100
            n = (n + (l % 100)) % 100

        else:
            n = 100 if n == 0 else n
            c += abs(n - 100 - l) // 100
            n = (n - (l % 100)) % 100

    return c

data = GetInput()

ans = Part1(data)
print(ans)

ans = Part2(data)
print(ans)