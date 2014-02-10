#!/usr/bin/env python3
"""
total(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3, b=4) _reps times, and returns total time for all runs, with final result.

bestof(spam, 1, 2, a=3, b=4, _reps=5) runs best-of-N timer to attempt to filter out system load variation, and returns best time among _reps tests.

bestoftotal(spam, 1, 2, a=3, b=4, _rep1=5, _reps=1000) runs best-of-totals test, which takes the best among _reps1 runs of (the total of _reps runs)
"""

import time, sys

try:
    timer = time.perf_counter
except AttributeError:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)
    repslist = list(range(_reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 5)
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        best = min(elapsed, best)
    return (best, ret)

def bestoftotal(func, *pargs, **kargs):
    _reps1 = kargs.pop('_reps1', 5)
    return min(total(func, *pargs, **kargs) for i in range(_reps1))


if __name__ == '__main__':
    print(total(pow, 2, 1000)[0])
    print(total(pow, 2, 1000, _reps=1000)[0])
    print(bestof(pow, 2, 100000)[0])
    print(bestoftotal(str.upper, 'spam', _reps1=30, _reps=1000)[0])
