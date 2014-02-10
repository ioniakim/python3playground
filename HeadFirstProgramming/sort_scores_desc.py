#!/usr/bin/env python3

scorelist = []

with open('results.txt') as scorefile:
    scorefile.readline() # skip the title line
    for line in scorefile:
        name, scorestr = line.split()
        score = float(scorestr)
        i = 0
        for scoreitem in scorelist:
            if score > scoreitem[1]:
                break
            i += 1
        scorelist.insert(i, (name, score))

for name, score in scorelist:
    print('Surfer', name, 'scored', score)

            