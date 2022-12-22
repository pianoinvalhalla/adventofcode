#!/usr/bin/env python3

input = open('input.txt','r')
score = 0

ROCK = 1
PAPER = 2
SCISSORS = 3
# result = (me - opponent)%3
DRAW = 0
WIN = 1
LOSE = 2
LOSE_SCORE = 0
DRAW_SCORE = 3
WIN_SCORE = 6

for line in input:
    opponent = 0
    me = 0
    if line[0] == 'A':
        opponent = ROCK
    elif line[0] == 'B':
        opponent = PAPER
    elif line[0] == 'C':
        opponent = SCISSORS
    if line[2] == 'X':
        me = ROCK
    elif line[2] == 'Y':
        me = PAPER
    elif line[2] == 'Z':
        me = SCISSORS
    score += me
    
    result = (me - opponent)%3
    
    if result == DRAW:
        score += DRAW_SCORE
    elif result == WIN:
        score += WIN_SCORE
    elif result == LOSE:
        score += LOSE_SCORE
        
print(score)
