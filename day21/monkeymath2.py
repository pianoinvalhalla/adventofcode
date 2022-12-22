#!/usr/bin/env python3

"""monkeymath2.py: Solution to Advent of Code 2022 Day 21, Part 2
Advent of Code can be found at https://adventofcode.com/2022"""

__author__ = "Vincent Mateo"
__email__ = "pianoinvalhalla@gmail.com"

input = open('input.txt','r')
jobs = {}

def yell(name):
#    if(name == 'humn'):
#        return 'h'
    expr = jobs[name]
    if expr == 'h':
        return 'h'
    output = ''
    try:
        return str(int(expr))
    except:
#        print(expr[:4] + expr[5] + expr[7:])
        output = "(" + yell(expr[:4]) + expr[5] + yell(expr[7:]) + ")"
        try:
            return str(eval(output))
        except:
            return output
        
def build(name):
    expr = jobs[name]
    if expr == 'h':
        return 'h'
    try:
        return int(expr)
    except:
        return [expr[5],build(expr[:4]),build(expr[7:])]

def simplify(node):
    if node == 'h':
        return 'h'
    try:
        left = int(node[1])
    except:
        left = simplify(node[1])
    try:
        right = int(node[2])
    except:
        right = simplify(node[2])
    try:
        return eval(str(int(left)) + node[0] + str(int(right)))
    except:
        return [node[0],left,right]

def solvestep(node):
    if node[0] != '=':
        raise Exception('invalid input tuple, no =')
    #validate that either node[1] or node[2] is a number
    try:
        number = int(node[1])
        expression = node[2]
    except:
        number = int(node[2])
        expression = node[1]
    if expression[0] == '+':
        #validate that either algebra[1] or algebra[2] is a number
        try:
            constant = int(expression[1])
            variable = expression[2]
        except:
            constant = int(expression[2])
            variable = expression[1]
        return ['=',variable,number-constant]
    elif expression[0] == '*':
        try:
            constant = int(expression[1])
            variable = expression[2]
        except:
            constant = int(expression[2])
            variable = expression[1]
        return ['=',variable,number/constant]
    elif expression[0] == '-':
        try:
            constant = int(expression[1])
            variable = expression[2]
            return ['=',variable,constant-number]
        except:
            constant = int(expression[2])
            variable = expression[1]
            return ['=',variable,number+constant]
    elif expression[0] == '/':
        try:
            constant = int(expression[1])
            variable = expression[2]
            return ['=',variable,constant/number]
        except:
            constant = int(expression[2])
            variable = expression[1]
            return ['=',variable,number*constant]
    raise Exception('could not solve'+node)

def solve(node):
    output = node
    while 1:
        try:
            output = solvestep(output)
        except:
            return output
    

#read input file into dictionary
for line in input:
    jobs[line[:4]] = line[6:17]

jobs['root'] = 'bhft = pzqf'
jobs['humn'] = 'h'
    
#print(jobs['root'])
#print(yell('root'))
#print(yell('bhft'))
rootnode = build('root')
#print(rootnode)
simple = simplify(rootnode)

#print(simplify(['+',1,1]))
#print(simplify(['*', 2, ['-', 'h', 3]]))

#print(solvestep(['=',2,['/',10,'h']]))
print(solve(simple))
