#!/usr/bin/env python3

"""monkeymath.py: Solution to Advent of Code 2022 Day 21, Part 1
Advent of Code can be found at https://adventofcode.com/2022"""

__author__ = "Vincent Mateo"
__email__ = "pianoinvalhalla@gmail.com"

input = open('input.txt','r')
jobs = {}

def yell(name):
    expr = jobs[name]
    try:
        return str(int(expr))
    except:
#        print(expr[:4] + expr[5] + expr[7:])
        return str(eval(yell(expr[:4]) + expr[5] + yell(expr[7:])))
        
    

#read input file into dictionary
for line in input:
    jobs[line[:4]] = line[6:17]
    
#print(jobs['root'])
print(yell('root'))

#part 2
jobs['humn'] = 3451534022348
print(yell('bhft'))
print(yell('pzqf'))
