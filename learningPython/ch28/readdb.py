#!/usr/bin/env python3

import shelve

db = shelve.open('persondb')
for key in sorted(db):
    print(key, '=>', db[key])

db.close()
