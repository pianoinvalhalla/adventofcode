#!/usr/bin/env python3

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
