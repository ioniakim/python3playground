#!/usr/bin/env python3


def intersect_arbitrarylist(*args):
    
    res = list()
    for x in args[0]:
        if x in res : continue
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)

    return res


def union_arbitrarylist(*args):
    
    res = list()
    for l in args:
        for x in l:
            if x not in res:
                res.append(x)

    return res

def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace : print(items)
        print(sorted(func(*items)))

if __name__ == '__main__':
    
    s1, s2, s3 = 'SPAM', 'SCAM', 'SLAM'

    print(intersect_arbitrarylist(s1, s2))
    print(union_arbitrarylist(s1, s2))
    print(intersect_arbitrarylist(s1, s2, s3))
    print(union_arbitrarylist(s1, s2, s3))

    tester(intersect_arbitrarylist, ('a', 'abcdefg', 'abdst', 'albmcnd'))
