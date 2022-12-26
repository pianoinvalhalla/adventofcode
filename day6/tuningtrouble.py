#!/usr/bin/env python3

"""tuningtrouble.py: Solution to Advent of Code 2022 Day 6, Part 1 and 2
Advent of Code can be found at https://adventofcode.com/2022"""

__author__ = "Vincent Mateo"
__email__ = "pianoinvalhalla@gmail.com"

input = open('input.txt','r')

buffer = []
bufferlength = 14   #4 for part 1, 14 for part 2
readcount = 0

#read 3 characters
#for i in range(bufferlength-1)
#    buffer.append(input.read(1))

while True:
    
    #append new char
    buffer.append([input.read(1)])
    if buffer[-1][0] == '':
        break
    readcount += 1
    
    #check new char for sameness with older chars, newest first
    #if same, indicate with negative index
    for i in range(-2,-len(buffer)-1,-1):
        if buffer[-1][0] == buffer[i][0]:
            buffer[i].append(i)
    
    #if not enough chars, skip checks
    if len(buffer) < bufferlength:
        continue
    
    #check all sameness indicators
    marker = True
    for i in range(len(buffer)):
        if len(buffer[i]) != 1:
            marker = False
            break
    
    #check if marker has been found, i.e. no sameness
    if marker:
        print(readcount)
        break
    
    #pop oldest char
    buffer.pop(0)
    
    #adjust sameness indicator and remove indicators corresponding to oldest char
    for i in range(len(buffer)):
        try:
            buffer[i][1] -= 1
            if buffer[i][1] < -len(buffer)-1:
                buffer[i].pop()
        except IndexError:
            pass
    

input.close()
