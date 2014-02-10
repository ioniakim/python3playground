#!/usr/bin/env python3

scores = {}

with open('results.txt') as f:
    f.readline()
    for line in f:
        name, score = line.split()
        scores[float(score)] = name

for score in sorted(scores.keys(), reverse=True):
    print('Surfer', scores[score], 'scored', score)