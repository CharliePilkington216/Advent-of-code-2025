import os

def GetInput():
    with open(os.getcwd() + "/input.txt") as file:
        points = [tuple(map(int, x.strip().split(','))) for x in file.readlines()]
    return points

def Dist(a,b):
    return (b[0] - a[0])**2 + (b[1] - a[1])**2 + (b[2] - a[2])**2

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

def SubGraphs(E, V):
    P = dict(zip(V, [-1 for _ in range(len(V))]))
    E = [x[1] for x in E]
    S = list()
    
    for e in E:
        v1 = e[0]
        v2 = e[1]
        
        if P[v1] == -1 and P[v2] == -1:
            n = len(S)
            P[v1] = n
            P[v2] = n
            S.append(set({v1, v2}))
            
        elif P[v1] == -1:
            S[P[v2]].add(v1)
            P[v1] = P[v2]

        elif P[v2] == -1:
            S[P[v1]].add(v2)
            P[v2] = P[v1]

        elif P[v1] != P[v2]:
            S[P[v1]] = S[P[v1]].union(S[P[v2]])
            for v in S[P[v2]]:
                P[v] = P[v1]            
            
    return S

def Calc(S):
    nums = set()
    for x in S:
        if x is not None:
            nums.add(len(x))

    total = 1
    for x in nums:
        total *= x
    return total

def Part1(V, n):
    E = GetDists(V, n)
    S = SubGraphs(E, V)
    return Calc(S)
    
                        
V = GetInput()

ans = Part1(V, 1000)
print(ans)


