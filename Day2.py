import os
import re

def GetInput():
    with open(os.getcwd() + '/input.txt') as file:
        data = list([x.strip() for x in file.read().split(',')])
    return data

def Search(domain, pattern):
    lower, upper = map(int, domain.split('-'))
    total = 0
    for x in range(lower, upper + 1):
        if pattern.match(str(x)):
            total += x
    return total

def Part1(data):
    count = 0
    pattern = re.compile(r'^(.+)\1{1}$')
    for line in data:
        count += Search(line, pattern)
    return count

def Part2(data):
    count = 0
    pattern = re.compile(r'^(.+)\1+$')
    for line in data:
        count += Search(line, pattern)
    return count

data = GetInput()
ans = Part1(data)
print(ans)

ans = Part2(data)
print(ans)
