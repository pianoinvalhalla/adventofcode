#!/usr/bin/env python3

"""campcleanup.py: Solution to Advent of Code 2022 Day 4, Part 1
Advent of Code can be found at https://adventofcode.com/2022"""

__author__ = "Vincent Mateo"
__email__ = "pianoinvalhalla@gmail.com"

import re

input = open('input.txt','r')
count = 0

for line in input:
    assignment = re.findall('\d+',line)
    #first assignment fully contains second assignment
    if int(assignment[0]) <= int(assignment[2]) and int(assignment[1]) >= int(assignment[3]):
        count += 1
    #second assignment fully contains first assignment
    elif int(assignment[2]) <= int(assignment[0]) and int(assignment[3]) >= int(assignment[1]):
        count += 1

print(count)

input.close()
