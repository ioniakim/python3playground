#!/usr/bin/env python3
"""
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-total time
"""
import time, sys

try:
    timer = time.perf_counter
except AttributeError:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

# def timer(func, *args):
#     start = time.time()
#     for i in range(1000):
#         func(*args)
#     return time.time() - start


def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)

    elapsed = timer() - start
    return (elapsed, ret)


def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    """
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        best = min(best, elapsed)

    return (best, ret)


def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)





if __name__ == '__main__':

    # print(timer(pow, 2, 1000))
    # print(timer(str.upper, 'spam'))

    print(total(1000, pow, 2, 1000)[0])
    print(total(1000, str.upper, 'spam')[0])

    print(bestof(1000, str.upper, 'spam'))

    print(bestof(50, total, 1000, str.upper, 'spam'))
    print(bestoftotal(50, 1000, str.upper, 'spam'))
    print(min(total(1000, str.upper, 'spam') for i in range(50)))
