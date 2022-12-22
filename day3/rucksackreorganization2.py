#!/usr/bin/env python3

input = open('input.txt','r')

def priority(char):
    output = ord(char)
    if output >= 65 and output < 91:
        output = output - ord('A') + 27
    elif output >= 97 and output < 123:
        output = output - ord('a') + 1
    else:
        raise Exception('invalid input')
    return output
    
sum = 0

elf = [input.readline(),input.readline(),input.readline()]
while (elf[0] != ''):
    common = 0
    for i in elf[0]:
        if common != 0:
            break
        for j in elf[1]:
            if common != 0:
                break
            if i == j:
                for k in elf[2]:
                    if i == k:
                        common = i
#                        print(common)
                        break
    sum += priority(common)
    elf = [input.readline(),input.readline(),input.readline()]
    
print(sum)
