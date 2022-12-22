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

for line in input:
    first = line[:(len(line)//2)]
    second = line[(len(line)//2):] #watch out for /n
    common = 0
    for charF in first:
        for charS in second:
            if charF == charS:
                common = charF
#    print(common)
#    print(priority(common))
    sum += priority(common)
#    print(first)
#    print(second)
print(sum)
