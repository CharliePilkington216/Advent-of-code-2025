import os

def GetInput():
    fresh = list()
    with open(os.getcwd() + '/input.txt') as file:
        line = file.readline().strip()
        while line != "":
            fresh.append(tuple(map(int, line.split('-'))))
            line = file.readline().strip()
        items = list([int(x.strip()) for x in file.readlines()])
    return fresh, items

def Corrected(fresh):
    fresh = sorted(fresh)
    
    i = 1
    prev = fresh[0]
    while i < len(fresh):      
        this = fresh[i]
        
        if this[0] <= prev[1] and this[1] >= prev[1]:
            i -= 1
            fresh.pop(i)
            fresh.pop(i)
            fresh.insert(i, (prev[0], this[1]))
            this = fresh[i]
            
        elif this[0] < prev[1] and this[1] < prev[1]:
            fresh.pop(i)
            i -= 1
            this = fresh[i]
            
        prev = this
        i += 1
    return fresh

def Search(item, fresh):
    a = 0
    b = len(fresh)
    while b > a:
        m = (a + b) // 2
        if item < fresh[m][0]:
            b = m
        elif item > fresh[m][1]:
            a = m + 1
        else:
            return 1
    return 0

def Range(tup):
    return tup[1] - tup[0] + 1

def Part1(items, fresh):
    return sum([Search(item, fresh) for item in items])

def Part2(fresh):
    return sum([Range(tup) for tup in fresh])    

fresh, items = GetInput()
fresh = Corrected(fresh)
ans = Part1(items, fresh)
print(ans)

ans = Part2(fresh)
print(ans)




