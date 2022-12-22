#!/usr/bin/env python3

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
