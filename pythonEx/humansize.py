#!/usr/bin/env python3
# -*- coding:utf-8 -*-

SUFFIXES = {1000:['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024:['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def approximate_size(size, a_kb_is_1024=True):
    '''Convert a file size to human-readbale form.
    Keyword arguments:
    size -- file size in bytes
    a_kb_is_1024 -- if True (default), use multiples of 1024
                 if False, use multiples of 1000

    Returns: string
    '''

    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kb_is_1024 else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')


if __name__ == '__main__':
    print(approximate_size(10000000000, False))
    print(approximate_size(10000000000))
