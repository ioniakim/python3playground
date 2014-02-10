#!/usr/bin/env python3
"Test the relative speed of iteration tool alternatives."

import sys, ch21_timer2

reps = 10000
repslist = list(range(reps))

def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]


def mapCall():
    return list(map(abs, repslist))

def genExpr():
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)

    return list(gen())

print(sys.version)

for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, result) = ch21_timer2.bestoftotal(test, _reps1=5, _reps=1000)
    print('%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1]))
