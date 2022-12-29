#!/usr/bin/env python3

"""proboscideavolcanium.py: Solution to Advent of Code 2022 Day 16, Part 1
Advent of Code can be found at https://adventofcode.com/2022"""

__author__ = "Vincent Mateo"
__email__ = "pianoinvalhalla@gmail.com"

class Valve:
    def __init__(self,name,flowrate=0,tunnels=[]):
        self.name = name
        self.flowrate = flowrate
        self.tunnels = tunnels
    def __lt__(self,valve2):
        return self.flowrate < valve2.flowrate

class State:
    def __init__(self,openvalves=set(),current='AA',minutes=0,pressure=0):
        self.openvalves = openvalves.copy()
        self.current = current
        self.minutes = minutes
        self.pressure = pressure
    def copy(self):
        return State(self.openvalves,self.current,self.minutes,self.pressure)
    def step(self,valvedict):
        state = self.copy()
        if state.minutes > 0:
            state.minutes -= 1
            for name in state.openvalves:
                state.pressure += valvedict[name].flowrate
    #            print('adding')
        return state
    def __lt__(self,state2):
#        if self.minutes == 0 and state.minutes == 0:
#            print('r')
        if self.minutes != state2.minutes:
            return self.minutes < state2.minutes
#            print('r')
        else:
            return self.pressure < state2.pressure
#        else:
#            return False
    def encode(self,sortedvalves):
        output = self.current
        for valve in sortedvalves:
            if valve.name in self.openvalves:
                output += valve.name
        return output

class Maximizer:
    def __init__(self,valvedict,minutes=30):
        self.valvedict = valvedict
        self.state = State(set(),'AA',minutes)
        self.best = State()
        self.sortedvalves = [valve for valve in self.valvedict.values() if valve.flowrate != 0]
#        self.sortedvalves = list(self.valvedict.values())
        self.sortedvalves.sort()
#        for valve in self.sortedvalves:
#            print(valve.name)
        self.dp = {}
    def upperbound(self,state):
        state = state.copy()
        sortedvalves = self.sortedvalves.copy()
        sortedvalves = [valve for valve in sortedvalves if valve.name not in state.openvalves]
#        for i in range(len(sortedvalves)):
#            if sortedvalves[i] in state.openvalves:
#                pop(i)
#        for name in self.valvedict:
#            state.openvalves.add(name)
#        while state.minutes > 0:
#            state = state.step(self.valvedict)
        while state.minutes > 0:
            #open highest-value valve
            try:
                state.openvalves.add(sortedvalves[-1].name)
                sortedvalves.pop(-1)
            except:
                pass
            for i in [0,1]:
                if state.minutes > 0:
                    state = state.step(self.valvedict)
#        print(state.pressure)
        return state
    def isredundant(self,state):
        code = state.encode(self.sortedvalves)
        output = False
        try:
            if state < self.dp[code]:
                output = True
#                print('r')
            elif self.dp[code] < state:
                self.dp[code] = state
        except:
            self.dp[code] = state
        return output
        
        
    def maximize(self):
        return self.maximizehelp(self.state)
    def maximizehelp(self,state):
        state = state.copy()
        if self.upperbound(state) < self.best:
            return State()
        if self.isredundant(state):
            return State()
        elif state.minutes <= 0:
            return state
        elif state.minutes == 1:
            state = state.step(self.valvedict)
#            print(state.pressure)
            return state
        state = state.step(self.valvedict)
#        state.minutes -= 1
        maxstate = State()
        #option: open current valve
        if not state.current in state.openvalves and self.valvedict[state.current].flowrate != 0:
            newstate = state.copy()
            newstate.openvalves.add(newstate.current)
            newstate = self.maximizehelp(newstate)
            if maxstate < newstate:
                maxstate = newstate
        #option: move to new valve
        for name in self.valvedict[state.current].tunnels:
            newstate = state.copy()
            newstate.current = name
            newstate = self.maximizehelp(newstate)
            if maxstate < newstate:
                maxstate = newstate
        #option: do nothing
        while (state.minutes > 0):
            state = state.step(self.valvedict)
#        output = state.pressure
        if maxstate < state:
            maxstate = state
#        print(maxstate.pressure)
        if self.best < maxstate:
            self.best = maxstate
        return maxstate
        
    

input = open('input.txt','r')

#read input file
valvedict = {}
for line in input:
    line = line.split('\n')[0]
    
    line0 = line.split('; ')
    name = line0[0][6:8]
    flowrate = int(line0[0].split('=')[1])\
    
    line1 = line0[1].split(', ')
    tunnels = []
    for tunnel in line1:
        tunnels.append(tunnel[-2:])
    valve = Valve(name,flowrate,tunnels)
    valvedict[name] = valve

#print(valvedict['AA'])

#for name in valvedict:
#    print(valvedict[name].name)

maximizer = Maximizer(valvedict,30)
#state = State({'BB','DD','EE','HH','JJ'},'CC',7,1086)
#state = State({'BB','DD','HH','JJ'},'EE',10,852)
#state = State({'BB','DD','HH','JJ'},'FF',11,776)
#state = State({'BB','DD','HH','JJ'},'GG',12,700)
#state = State({'BB','DD','JJ'},'GG',15,516)
#state = State({'BB','DD','JJ'},'DD',18,354)
#result = maximizer.maximizehelp(state)
result = maximizer.maximize()
print(result.pressure)
print(result.openvalves)

input.close()
