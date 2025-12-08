import os

def GetInput():
    with open(os.getcwd() + "\\input.txt") as file:
        points = [tuple(map(int, x.strip().split(','))) for x in file.readlines()]
    return points

def Dist(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2

def GetDists(points, n):
    weighted_edges = list()
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = Dist(points[i], points[j])
            if len(weighted_edges) < n or d < weighted_edges[n - 1][0]:
                weighted_edges.insert(Insert(weighted_edges, d), (d, (points[i], points[j])))
            if len(weighted_edges) > n:
                weighted_edges.pop(-1)
    return weighted_edges

def Insert(array, item):
    a = 0
    b = len(array)
    while b > a:
        m = (a + b) // 2
        if array[m][0] > item:
            b = m
        elif array[m][0] < item:
            a = m + 1
        else:
            return m
    return a

def Point(S, n):
    while type(S[n]) == int:
        n = S[n]
    return n

def Calc(E, V):
    G = dict(zip(V, [i + 1 for i in range(len(V))]))
    E = [x[1] for x in E]

    for e in E:
        if G[e[0]] != G[e[1]]:
            group = G[e[1]]
            for v in V:
                if G[v] == group:
                    G[v] = G[e[0]]

    nums = [0 for _ in range(len(V))]
    for v in V:
        nums[G[v] - 1] += 1

    nums.sort()
    return nums[-1] * nums[-2] * nums[-3]

def FullyConnect(V, E):
    G = dict(zip(V, [i + 1 for i in range(len(V))]))
    E = [x[1] for x in E]
    i = 0
    while len(set(G.values())) != 1:
        e = E[i]
        group = G[e[1]]
        for v in V:
            if G[v] == group:
                G[v] = G[e[0]]

        i += 1

    return e[0][0] * e[1][0]

def Part1(V, n):
    E = GetDists(V, n)
    return Calc(E, V)

def Part2(V):
    n = (len(V)*(len(V) - 1) / 2) + 2
    E = GetDists(V, n)
    return FullyConnect(V, E)

V = GetInput()

ans = Part1(V, 1000)
print(ans)

ans = Part2(V)
print(ans)