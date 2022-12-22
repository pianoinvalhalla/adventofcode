#!/usr/bin/env python3

"""caloriecounting2.py: Solution to Advent of Code 2022 Day 1, Part 2
Advent of Code can be found at https://adventofcode.com/2022"""

__author__ = "Vincent Mateo"
__email__ = "pianoinvalhalla@gmail.com"

input = open('input.txt','r')
calories = 0
mostCalories = [0,0,0]
for line in input:
    try:
        calories += int(line)
#        print(int(line))
    except:
        if calories > mostCalories[0]:
            mostCalories[2] = mostCalories[1]
            mostCalories[1] = mostCalories[0]
            mostCalories[0] = calories
        elif calories > mostCalories[1]:
            mostCalories[2] = mostCalories[1]
            mostCalories[1] = calories
        elif calories > mostCalories[2]:
            mostCalories[2] = calories
        print(calories)
        calories = 0
print('')
print(mostCalories)
print(mostCalories[0]+mostCalories[1]+mostCalories[2])
