#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
from os.path import *
import re
import os


def encoding2coding(file):
    pattern = r'(?P<prefix>^#\s*-\*-\s*)encoding(?P<postfix>\s*:utf-8\s*-\*-\s*$)'
    rep = r'\g<prefix>coding\g<postfix>'
    lines = []

    with open(file, 'r') as f:
        lines = f.readlines()

    with open(file, 'w') as f:
        for line in lines:
            if re.match(pattern, line):
                f.write(re.sub(pattern, rep, line))
            else:
                f.write(line)


    
if len(sys.argv) < 2 :
    print('File names are required')
    exit(1)


    
for file in sys.argv[1:]:
    if isfile(file) == True :
        encoding2coding(file)
