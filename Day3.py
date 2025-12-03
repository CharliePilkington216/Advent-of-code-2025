import os

def GetInput():
    with open(os.getcwd() + '/input.txt') as file:
        data = list([x.strip() for x in file.readlines()])
    return data

def Part1(data):
    total = 0
    for bank in data:
        highest = "0"
        next_highest = "0"

        for battery in bank[:-1]:
            if battery > highest:
                highest = battery
                next_highest = "0"
            elif battery > next_highest:
                next_highest = battery

        if bank[-1] > next_highest:
            next_highest = bank[-1]

        total += int(highest + next_highest)

    return total

def Part2(data, n):
    total = 0
    for bank in data:
        num = ["0" for _ in range(n)]
        m = len(bank)
        
        for i in range(0, m):
            
            j = n
            while j > 0:
                
                if bank[i] > num[j - 1] and m - i >= j:
                    num[j - 1] = bank[i]
                    j -= 1
                    while j > 0:
                        num[j - 1] = "0"
                        j -= 1
                j -= 1
                        
        total += int(''.join(num[::-1]))

    return total
    
data = GetInput()
ans = Part1(data)
print(ans)

ans = Part2(data, 12)
print(ans)
