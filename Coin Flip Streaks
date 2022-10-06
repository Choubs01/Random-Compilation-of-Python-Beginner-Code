# This is a program to find out how often a streak of heads or a streak of six tails comes up in a randomly generated list of heads and tails.
import random

x = 0
z = 0
y = 0
h = 0

for sixHTs in range(10000):
    for HTs in range(100):
        if random.randint(0,1) == 1: #H
            x += 1
            y = 0
            if x == 13: #Check for streak of H
                z += 1
        else: #T
            y += 1
            x = 0
            if y == 13: #Check for streak to T
                h +=1

print('A 13 streak of heads occured', z, "times." )
print('A 13 streak of tails occured', h, 'times.')
