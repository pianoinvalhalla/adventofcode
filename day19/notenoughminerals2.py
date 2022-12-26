#!/usr/bin/env python3

"""notenoughminerals2.py: Solution to Advent of Code 2022 Day 19, Part 1 and 2
Advent of Code can be found at https://adventofcode.com/2022"""

__author__ = "Vincent Mateo"
__email__ = "pianoinvalhalla@gmail.com"

import re

input = open('input.txt','r')

class ResourceList(tuple):
    def printdescription(self):
        print(str(self[0])+' ore')
        print(str(self[1])+' clay')
        print(str(self[2])+' obsidian')
        print(str(self[3])+' geode')
    def __add__(self,list2):
        return ResourceList(x+y for x,y in zip(self,list2))
    def __sub__(self,list2):
        return ResourceList(x-y for x,y in zip(self,list2))
    def isnegative(self):
        return self[0]<0 or self[1]<0 or self[2]<0 or self[3]<0
    def __le__(self,list2):
        return self[0]<=list2[0] and self[1]<=list2[1] and self[2]<=list2[2] and self[3]<=list2[3]
    def __mul__(self,scalar):
        return ResourceList(n*scalar for n in self)

class Blueprint(ResourceList):
    def printdescription(self):
        print('Each ore robot costs '+str(self[0])+' ore.')
        print('Each clay robot costs '+str(self[1])+' ore.')
        print('Each obsidian robot costs '+str(self[2][0])+' ore and '+str(self[2][1])+' clay.')
        print('Each geode robot costs '+str(self[3][0])+' ore and '+str(self[3][1])+' obsidian.')
    def robotcost(self,robotlist):
        ore = robotlist[0]*self[0] + robotlist[1]*self[1] + robotlist[2]*self[2][0] + robotlist[3]*self[3][0]
        clay = robotlist[2]*self[2][1]
        obsidian = robotlist[3]*self[3][1]
        return ResourceList((ore,clay,obsidian,0))

class MaximizerState:
    def __init__(self,robots,resources,minutes):
        self.robots = ResourceList(robots)
        self.resources = ResourceList(resources)
        self.minutes = minutes
    def copy(self):
        return MaximizerState(self.robots,self.resources,self.minutes)

class MaximizerNode:
    def __init__(self,state):
        self.state = state.copy()
        self.children = []

class MaximizerTwo:
    def __init__(self,blueprint,state):
        self.blueprint = blueprint
        self.mycount = 0
        self.state = state
        self.best = MaximizerState((0,0,0,0),(0,0,0,0),0)
    
    def maximizestep(self,state,newrobots):
        newstate = state.copy()
        
        #spend resources to build new robots
        newstate.resources -= blueprint.robotcost(newrobots)

        #check for no hope
        for i in range(len(newstate.resources)):
            if newstate.resources[i]<0 and newstate.robots[i] <= 0:
                raise Exception
        
        #do-nothing minutes to make up resource debt
        while (newstate.resources.isnegative()):
            newstate.resources += newstate.robots
            newstate.minutes -= 1
            if newstate.minutes < 0:
                raise Exception
            
        #collect resources
        newstate.resources += newstate.robots
        newstate.minutes -= 1
        if newstate.minutes < 0:
            raise Exception
        
        #new robots are ready
        newstate.robots += newrobots
        
        return newstate
    
    def maximize(self):
        return self.maximizehelp(self.state)
    
    def optimistic(self,state):
        newstate = state.copy()
        newstate.resources += state.robots * state.minutes
        #make a geode robot every minute
        #add a number of geodes equal to (minutes-1)+(minutes-2)+...+1
        newstate.resources += (0,0,0,state.minutes*state.minutes//2)
        newstate.minutes = 0
        return newstate
    
    def maximizehelp(self,state):
        if state.minutes <= 0:
            return state
        elif state.minutes == 1:
            return MaximizerState(state.robots,state.resources+state.robots,0)
        elif self.optimistic(state).resources[3] <= self.best.resources[3]:
            return MaximizerState((0,0,0,0),(0,0,0,0),0)
        else:
            #default is do-nothing
            maxstate =  MaximizerState(state.robots,state.resources+state.robots*state.minutes,0)
            
            possiblemoves = [(0,0,0,1)]
            if state.robots[2] < self.blueprint[3][1]:
                possiblemoves.append((0,0,1,0))
            if (
#                state.robots[2] == 0 and
                state.robots[1] < self.blueprint[2][1]):
                possiblemoves.append((0,1,0,0))
            if (
#                state.robots[1] == 0 and
            state.robots[0] < self.blueprint[1] or
                state.robots[0] < self.blueprint[2][0] or
                state.robots[0] < self.blueprint[3][0]):
                possiblemoves.append((1,0,0,0))
                
            for newrobots in possiblemoves[:state.minutes-1]:
                try:
                    newstate = self.maximizestep(state,newrobots)
                    newmax = self.maximizehelp(newstate)
                    self.mycount += 1
                    if newmax.resources[3] > maxstate.resources[3]:
                        maxstate = newmax
                    if newmax.resources[3] > self.best.resources[3]:
                        self.best = newmax
                except:
                    pass
            return maxstate
            
  
geodes = []

'''
#PART 1
#for line in input:
'''

#PART 2
for i in [0,1,2]:
    line = input.readline()
    
    numbers = re.findall('\d+',line)
    blueprint = None
    if numbers != '':
        blueprint = Blueprint((int(numbers[1]),int(numbers[2]),[int(numbers[3]),int(numbers[4])],[int(numbers[5]),int(numbers[6])]))
        blueprint.printdescription()

    '''
    #PART 1
    #state = MaximizerState((1,4,1,0),(2,11,2,0),11)
    #state = MaximizerState((1,3,0,0),(4,15,0,0),14)
    #state = MaximizerState((1,3,0,0),(2,9,0,0),16)
    #state = MaximizerState((1,2,0,0),(2,4,0,0),18)
    #state = MaximizerState((1,1,0,0),(2,1,0,0),20)
    state = MaximizerState((1,0,0,0),(0,0,0,0),24)
    '''
    
    #PART 2
    state = MaximizerState((1,0,0,0),(0,0,0,0),32)
#    state = MaximizerState((1,0,0,0),(4,0,0,0),28)

    maximizer = MaximizerTwo(blueprint,state)
    finalstate = maximizer.maximize()
    finalstate.resources.printdescription()
    finalstate.robots.printdescription()
    geodes.append(finalstate.resources[3])

    print(maximizer.mycount)

input.close()

'''
#PART 1
qualitylevel = [x*y for x,y in zip(geodes,range(1,len(geodes)+1))]
print(geodes)
print(qualitylevel)
print(sum(qualitylevel))
'''

#PART 2
print(geodes)
print(geodes[0]*geodes[1]*geodes[2])
