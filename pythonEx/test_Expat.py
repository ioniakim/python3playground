#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.parsers.expat as expat


def start_element(name, attrs):
    print('Start element', name, attrs)

def char_data(data):
    print('Character data', repr(data))

pa = expat.ParserCreate()

pa.StartElementHandler = start_element
pa.CharacterDataHandler = char_data



with open('./book.xml', 'rb') as book:
    pa.ParseFile(book)