import os

def GetInput():
    with open(os.getcwd() + "\\input.txt") as file:
        data = [x.strip().split() for x in file.readlines()]
    return data

def Format1(data):
    values = list(map(Initialise, data[-1]))
    operators = list(map(Assign, data[-1]))
    data = [list(map(int, x)) for x in data[:-1]]
    return data, operators, values

def Format2():
    with open(os.getcwd() + "\\input.txt") as file:
        data = [x.rstrip() for x in file.readlines()]
    inits = list(map(Initialise, data[-1].strip().split()))
    operators = list(map(Assign, data[-1].strip().split()))
    data = data[:-1]
    values = list([[]])
    k = 0

    n = len(data)
    m = Max(data)
    data = Correct(data, m)
    for i in range(m):
        num = ""
        for j in range(n):
            num += data[j][i]
        num = num.replace(' ','')
        if num != '':
            values[k].append(int(num))
        else:
            values.append([])
            k += 1
    return values, operators, inits

def Max(data):
    highest = 0
    for line in data:
        if len(line) > highest:
            highest = len(line)
    return highest

def Correct(data, n):
    new_data = list()
    for line in data:
        new_data.append(''.join(line).ljust(n, ' '))
    return new_data

def Initialise(operator):
    if operator == "*":
        return 1
    else:
        return 0

def Assign(operator):
    if operator == "*":
        return Multiply
    else:
        return Add

def Add(x, y):
    return x + y

def Multiply(x, y):
    return x * y

def Part1(data):
    data, operators, values = Format1(data)
    n = len(operators)
    for line in data:
        for i in range(n):
            values[i] = operators[i](line[i], values[i])
    return sum(values)

def Part2():
    data, operators, values = Format2()
    n = len(data)
    for i in range(n):
        for num in data[i]:
            values[i] = operators[i](values[i], num)
    return sum(values)


data = GetInput()
ans = Part1(data)
print(ans)

ans = Part2()
print(ans)



