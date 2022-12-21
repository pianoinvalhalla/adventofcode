#!/usr/bin/env python3

input = open('input.txt','r')
calories = 0
mostCalories = 0
for line in input:
    try:
        calories += int(line)
#        print int(line)
    except:
        if calories > mostCalories:
            mostCalories = calories
        print calories
        calories = 0
print ''
print mostCalories
