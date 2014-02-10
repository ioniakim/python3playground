#!/usr/bin/env python3

def find_details(id):

    with open('rsa.txt') as f:
        for line in f:
            s = {}
            (s['id'], s['name'], s['country'], s['average'],s['type'], s['age']) = line.split(';')
            if s['id'] == id:
                return s

    return None

    
while True:
    id = input('enter id (enter q to quit): ')

    if id == 'q':
        break

    s = find_details(id)
    if s != None:
        print('ID:         ', s['id'])
        print('Name:       ', s['name'])
        print('Country:    ', s['country'])
        print('Average:    ', s['average'])
        print('Board type: ', s['type'])
        print('Age:        ', s['age'])
    else:
        print('ID', id, 'is not valid.')
        









