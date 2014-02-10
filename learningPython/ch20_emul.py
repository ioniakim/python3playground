#!/usr/bin/env python3

# emulating zip and map with iteration tools

def mymap_list1(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res

def mymap_list2(func, *seqs):
    return [func(*args) for args in zip(*seqs)]


def mymap_gen1(func, *seqs):
    for args in zip(*seqs):
        yield func(*args)

def mymap_gen2(func, *seqs):
    return (func(*args) for args in zip(*seqs))


# truncating zip
def myzip_list1(*seqs):
    seqs = [list(s) for s in seqs]
    res = []
    while all(seqs):
        res.append(tuple(s.pop(0) for s in seqs))
    return res

def myzip_list2(*seqs):
    minlen = min(len(s) for s in seqs)
    return [tuple(s[i] for s in seqs) for i in range(minlen)]


def myzip_gen1(*seqs):
    seqs = [list(s) for s in seqs]
    while all(seqs):
        yield tuple(s.pop(0) for s in seqs)


def myzip_gen2(*seqs):
    minlen = min(len(s) for s in seqs)
    return (tuple(s[i] for s in seqs) for i in range(minlen))


def myzip_gen3(*seqs):
    iters = list(map(iter, seqs))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)

    

def mymapPad_list1(*seqs, pad=None):
    ''' 2.X padding map
    '''
    seqs = [list(s) for s in seqs]
    res = []
    while any(seqs):
        res.append(tuple((s.pop(0) if s else pad) for s in seqs))
    return res

def mymapPad_list2(*seqs, pad=None):
    maxlen = max(len(s) for s in seqs)
    return [tuple((s[i] if i < len(s) else pad) for s in seqs) for i in range(maxlen)]


def mymapPad_gen1(*seqs, pad=None):
    seqs = [list(s) for s in seqs]
    while any(seqs):
        yield tuple((s.pop(0) if s else pad) for s in seqs)


def mymapPad_gen2(*seqs, pad=None):
    maxlen = max(len(s) for s in seqs)
    return (tuple((s[i] if i < len(s) else pad) for s in seqs) for i in range(maxlen))


if __name__ == '__main__':

    l1 = [-2, -1, 0, 1, 2]
    l2 = [1, 2, 3]
    l3 = [2, 3, 4, 5]

    print(mymap_list1(abs, l1))
    print(mymap_list1(pow, l2, l3))

    print(mymap_list2(abs, l1))
    print(mymap_list2(pow, l2, l3))

    print(list(mymap_gen1(abs, l1)))
    print(list(mymap_gen1(pow, l2, l3)))

    print(list(mymap_gen2(abs, l1)))
    print(list(mymap_gen2(pow, l2, l3)))

    s1, s2 = 'abc', 'xyz123'
    print(myzip_list1(s1, s2))
    print(mymapPad_list1(s1, s2))

    print(list(myzip_gen1(s1, s2)))
    print(list(mymapPad_gen1(s1, s2)))

    print(myzip_list2(s1, s2))
    print(list(myzip_gen2(s1, s2)))

    print(mymapPad_list2(s1, s2))
    print(list(mymapPad_gen2(s1, s2)))

    print(list(myzip_gen3(s1, s2)))
