import os

def GetInput():
    graph = dict()
    with open(os.getcwd() + "/input.txt") as file:
        for line in file.readlines():
            vertex, edges = line.strip().split(':')
            edges = set(edges.strip().split())
            graph[vertex] = edges
    return graph

def Path1(vertex, prev_vertices, graph):    
    neighbours = graph[vertex]-prev_vertices
    if neighbours == set({}):
        return 0
    if neighbours == set({'out'}):
        return 1
    path = prev_vertices.union(set({vertex}))
    return sum(Path1(v, path, graph) for v in neighbours)

def Path2(vertex, prev_vertices, graph):    
    neighbours = graph[vertex]-prev_vertices
    path = prev_vertices.union(set({vertex}))

    print(vertex)
    print(path)
    
    if neighbours == set({}):
        return 0
    if neighbours == set({'out'}) and 'dac' in path and 'fft' in path:
        return 1
    if neighbours == set({'out'}):
        return 0
    return sum(Path2(v, path, graph) for v in neighbours)

def Part1(graph):
    return Path1('you', set({}), graph)

def Part2(graph):
    return Path2('svr', set({}), graph)

graph = GetInput()

ans = Part1(graph)
print(ans)

ans = Part2(graph)
print(ans)
