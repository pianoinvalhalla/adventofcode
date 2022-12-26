#!/usr/bin/env python3

"""supplystacks2.py: Solution to Advent of Code 2022 Day 5, Part 2
Advent of Code can be found at https://adventofcode.com/2022"""

__author__ = "Vincent Mateo"
__email__ = "pianoinvalhalla@gmail.com"

import re

input = open('input.txt','r')

#read stacks lines
lines = []
stackcount = 0
while True:
    lines.append(input.readline())
    #are we at stack numbers?
    stacknumbers = re.findall('\d+',lines[-1])
    if stacknumbers != []:
        stackcount = int(stacknumbers[-1])
        break
        
#initialize stacks 2d array
stacks = [None]
for j in range(1,stackcount+1):
    stacks.append([])

#store stacks data from bottom up
for i in range(len(lines)-1):
#    print(lines[-2-i])
    for j in range(1,stackcount+1):
        crate = lines[-2-i][4*j-3]
#        print(crate)
        if crate != ' ' and crate != '\n':
            stacks[j].append(crate)

#read and execute instructions
while True:
    line = input.readline()
#    print(line)
    if line == '':
        break
    instruction = re.findall('\d+',line)
    if instruction != []:
        count = int(instruction[0])
        stackfrom = int(instruction[1])
        stackto = int(instruction[2])
        crates = []
        for i in range(count):
            crates.append(stacks[stackfrom].pop())
        for i in range(count):
            stacks[stackto].append(crates.pop())

#output top crate in each stack
print(stacks)
output = ''
for j in range(1,stackcount+1):
    output += (stacks[j][-1])
print(output)
input.close()
