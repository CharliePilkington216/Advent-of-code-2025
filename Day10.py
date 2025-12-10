import os

class PriorityQueue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, item, priority):
        a = 0
        b = len(self.queue)
        while b > a:
            m = (a + b) // 2
            if self.queue[m][1] < priority:
                a = m + 1
            elif self.queue[m][1] > priority:
                b = m
            else:
                self.queue.insert(m, (item, priority))
                return None
        self.queue.insert(a, (item, priority))
        return None

    def dequeue(self):
        item = self.queue[0][0]
        self.queue.pop(0)
        return item

def GetInput():
    data = list()
    with open(os.getcwd() + "/input.txt") as file:
        for line in file.readlines():
            line = line.strip().split()

            k = len(line[0]) - 2
            target = int(line[0][1:-1].replace('.','0').replace('#','1'), 2)
            edges = list(tuple(map(int, tuple(x[1:-1].split(',')))) for x in line[1:-1])
            weights = list(map(int, list(line[-1][1:-1].split(','))))
            
            data.append((k, target, edges, weights))
    return data

def InitVertices(k):
    return tuple([None, False] for _ in range(pow(2, k)))

def ConvertEdges(edges, k):
    new_edges = list()
    for e in edges:
        num = 0
        for n in e:
            num += pow(2, k - n - 1)
        new_edges.append(num)
    return new_edges

def Dijsktra(vertices, edges, target):
    queue = PriorityQueue()
    vertices[0][0] = 0
    queue.enqueue(0,0)
    
    while not(vertices[target][1]):
        
        current = queue.dequeue()
        while vertices[current][1]:
            current = queue.dequeue()

        for i in range(len(edges)):
            
            neighbour = current ^ edges[i]

            if not(vertices[neighbour][1]):

                weight = vertices[current][0] + 1
                if vertices[neighbour][0] is None or vertices[neighbour][0] > weight:
                    
                    vertices[neighbour][0] = weight
                    queue.enqueue(neighbour, weight)

        vertices[current][1] = True

    return vertices[current][0]

def Part1(data):
    total = 0
    for line in data:
        vertices = InitVertices(line[0])
        target = line[1]
        edges = ConvertEdges(line[2], line[0])
        ans = Dijsktra(vertices, edges, target)

        total += ans

    return total
                

data = GetInput()

ans = Part1(data)
print(ans)


