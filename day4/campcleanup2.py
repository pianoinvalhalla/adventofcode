#!/usr/bin/env python3

"""campcleanup2.py: Solution to Advent of Code 2022 Day 4, Part 2
Advent of Code can be found at https://adventofcode.com/2022"""

__author__ = "Vincent Mateo"
__email__ = "pianoinvalhalla@gmail.com"

import re

input = open('input.txt','r')
count = 0

for line in input:
    #get assignments
    a = re.findall('\d+',line)
    for i in range(len(a)):
        a[i] = int(a[i])
    
    #check overlap
    if ((a[0] <= a[2] and a[2] <= a[1]) or
        (a[0] <= a[3] and a[3] <= a[1]) or
        (a[2] <= a[0] and a[0] <= a[3]) or
        (a[2] <= a[1] and a[1] <= a[3])):
        count += 1

print(count)

input.close()
