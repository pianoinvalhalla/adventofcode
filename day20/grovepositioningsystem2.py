#!/usr/bin/env python3

"""grovepositioningsystem2.py: Solution to Advent of Code 2022 Day 20, Part 2
Advent of Code can be found at https://adventofcode.com/2022"""

__author__ = "Vincent Mateo"
__email__ = "pianoinvalhalla@gmail.com"


#doubly linked list
class CoordinateNode:
    def __init__(self, coordinate, prev, next):
        self.coordinate = coordinate
        self.prev = prev
        self.next = next
        #also a singly linked list, whose order will be preserved after swaps in the doubly linked list
        self.ordernext = None
    def printlist(self):
        curr = self
        while True:
            print(curr.coordinate)
            curr = curr.next
            if (curr == self):
                break
            if (curr == None):
                break

input = open('input.txt','r')
DECRYPTION_KEY = 811589153

#READING INPUT FILE INTO DOUBLY/SINGLY LINKED LIST

#dummy head node
head = CoordinateNode(None,None,None)
prev = head
tail = None
length = 0

for line in input:
    tail = CoordinateNode(int(line)*DECRYPTION_KEY,prev,None)
    prev.next = tail
    prev.ordernext = tail
    prev = tail
    length += 1
lengthminusone = int(length - 1)
    
#switch dummy head node to actual head node
#link tail to head
head = head.next
head.prev = tail
tail.next = head

#head.printlist()
#print(length)





#MIXING BY ITERATING ON SINGLY LINKED LIST AND SWAPPING ON DOUBLY LINKED LIST
for j in range(10):
    curr = head
    while True:
    #    print(curr.coordinate)
        if curr.coordinate > 0 and curr.coordinate%(length-1) != 0:
            #move forward
            target = curr
            for i in range(curr.coordinate%(length-1)):
                target = target.next
                #fix off-by-one issue
    #                if (target == curr):
    #                    target = target.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            target.next.prev = curr
            curr.next = target.next
            curr.prev = target
            target.next = curr
        elif curr.coordinate < 0 and (-curr.coordinate)%(length-1) != 0:
            #move backward
            target = curr
            for i in range((-curr.coordinate)%(length-1)):
                target = target.prev
                #fix off-by-one issue
    #            if (target == curr):
    #                target = target.prev
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            target.prev.next = curr
            curr.prev = target.prev
            curr.next = target
            target.prev = curr
        
        curr = curr.ordernext
    #    if (curr == head):
    #        break
        if (curr == None):
            break
  
        
        
#curr = head
#print(head.coordinate)
#print(head.next.coordinate)
#print(head.prev.coordinate)

#head.printlist()



#FIND 0 COORDINATE, THEN ITERATE 1000/2000/3000 TIMES
curr = head
while True:
    if curr.coordinate == 0:
        break;
    curr = curr.next
    if (curr == head):
        break
    if (curr == None):
        break
        
print(curr.coordinate)
#print(str(curr.coordinate) + ' ' + str(curr.next.coordinate) + ' ' + str(curr.prev.coordinate))

sum = 0

for j in range(3):
    for i in range(1000):
        curr = curr.next
#        print(i)
    print(curr.coordinate)
    sum += curr.coordinate

print(sum)



#head.printlist()


#print(head.coordinate)
#print(head.next.coordinate)
#print(head.next.next.coordinate)
#print(head.prev.coordinate)
#print(head.prev.prev.coordinate)


