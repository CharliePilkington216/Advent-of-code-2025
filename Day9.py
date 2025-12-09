import os

def GetInput():
    with open(os.getcwd() + "/input.txt") as file:
        points = [tuple(map(int, line.split(','))) for line in file.readlines()]
    return points

def Lines(points):
    vertical = list()
    horizontal = list()
    n = len(points)
    index = 0
    current = points[0]
    while index < n:
        i = (index + 1) % n

        if current[1] > points[i][1]:
            vertical.append((current[0], (points[i][1], current[1])))

        elif current[1] < points[i][1]:
            vertical.append((current[0], (current[1], points[i][1])))

        elif current[0] > points[i][0]:
            horizontal.append(((points[i][0], current[0]), current[1]))

        elif current[0] < points[i][0]:
            horizontal.append(((current[0], points[i][0]), current[1]))

        current = points[i]

        index += 1

    return vertical, horizontal

def Intersect(a, b, vertical, horizontal):
    x0 = min(a[0], b[0])
    x1 = max(a[0], b[0])
    xm = ((x0 + x1) // 2)

    y0 = min(a[1], b[1])
    y1 = max(a[1], b[1])
    ym = ((y0 + y1) // 2)

    inside = False
    boundary = False

    for line in horizontal:
        if not(line[0][1] <= x0 or line[0][0] >= x1) and y0 < line[1] < y1:
            return 0

        if ym == line[1]:
            inside = True
            boundary = True

        elif not boundary and line[0][0] <= xm < line[0][1] and ym > line[1]:
            inside = not(inside)

    if not inside:
        return 0

    inside = False
    boundary = False

    for line in vertical:
        if not(line[1][1] <= y0 or line[1][0] >= y1) and x0 < line[0] < x1:
            return 0

        if xm == line[0]:
            inside = True
            boundary = True

        elif not boundary and line[1][0] <= ym < line[1][1] and xm > line[0]:
            inside = not (inside)

    if not inside:
        return 0

    return Area(a, b)

def Area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def Part1(points):
    n = len(points)
    highest_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            area = Area(points[i], points[j])
            if area > highest_area:
                highest_area = area
    return highest_area

def Part2(points):
    vertical, horizontal = Lines(points)
    n = len(points)
    highest_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            a, b = points[i], points[j]
            area = Intersect(points[i], points[j], vertical, horizontal)
            if area > highest_area:
                highest_area = area
    return highest_area

points = GetInput()

ans = Part1(points)
print(ans)

ans = Part2(points)
print(ans)
