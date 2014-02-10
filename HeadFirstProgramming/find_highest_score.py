#!/usr/bin/env python3

highest = 0.0

with open('results.txt') as result_f:
    for line in result_f:
        score = float(line)

        if highest < score:
            highest = score

print('Highest score: ', highest)


    