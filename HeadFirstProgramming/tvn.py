#!/usr/bin/env python3

import sqlite3

def find_details(id):
    
    db = sqlite3.connect('surfersDB.sdb')
    db.row_factory = sqlite3.Row
    cursor = db.cursor()
    cursor.execute('select * from surfers')

    rows = cursor.fetchall()

    for row in rows:
        if row['id'] == id:
            s = {}
            s['id'] = str(row['id'])
            s['name'] = row['name']
            s['country'] = row['country']
            s['average'] = str(row['average'])
            s['board'] = row['board']
            s['age'] = str(row['age'])
            cursor.close()
            return s
    return None


id = int(input('enter id: '))

s = find_details(id)

if s != None:
    print('ID:         ', s['id'])
    print('Name:       ', s['name'])
    print('Country:    ', s['country'])
    print('Average:    ', s['average'])
    print('Board type: ', s['board'])
    print('Age:        ', s['age'])
else:
    print('ID', id, 'is not valid.')
