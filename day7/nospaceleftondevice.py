#!/usr/bin/env python3

"""nospaceleftondevice.py: Solution to Advent of Code 2022 Day 7, Part 1 and 2
Advent of Code can be found at https://adventofcode.com/2022"""

__author__ = "Vincent Mateo"
__email__ = "pianoinvalhalla@gmail.com"

class Directory:
    def __init__(self,name):
        self.name = name
        self.ls = []
    def totalsize(self,list=[]):
        output = 0
        for child in self.ls:
            output += child.totalsize(list)[0]
        list.append(output)
        return output,list
            

class File:
    def __init__(self,size,name):
        self.size = int(size)
        self.name = name
    def totalsize(self,list=[]):
        return self.size,list

input = open('input.txt','r')

root = Directory('/')
path = [root]

#read input file and build tree
for line in input:
    args = line.split()
#    print(args)
    if args[0] == '$':
        if args[1] == 'ls':
            pass
        elif args[1] == 'cd':
            #TODO
            if args[2] == '/':
                path = [root]
            elif args[2] == '..':
                path.pop()
            else:
                found = False
                for child in path[-1].ls:
                    if child.name == args[2]:
                        path.append(child)
                        found = True
                        break
                if not found:
                    print('error')
                    for d in path:
                        print(d.name)
                    raise Exception
    elif args[0] == 'dir':
        newdirectory = Directory(args[1])
        path[-1].ls.append(newdirectory)
#        print(path[-1].ls)
    else:
        newfile = File(args[0],args[1])
        path[-1].ls.append(newfile)
        
'''
#PART 1
result = root.totalsize()
print(result)
sum = 0
for n in result[1]:
    if n <= 100000:
        sum += n
print(sum)
'''

#PART 2
DISK_SPACE = 70000000
UPDATE_SPACE = 30000000
result = root.totalsize()
freespace = DISK_SPACE - result[0]
deletesize = result[0]
for n in result[1]:
    if n+freespace >= UPDATE_SPACE and n < deletesize:
        deletesize = n
print(deletesize)
    

input.close()
