#!/usr/bin/env python3

highest = 0.0
student = ''

with open('results.txt') as result_f:
    line = result_f.readline() # skip the title line
    for line in result_f:
        name, score = line.split()
        if float(score) > highest:
            highest = float(score)
            student = name

print(name, highest)
