#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sqlite3

# test.db라는 파일에 DB파일 생성
# con = sqlite3.connect("test.db")

# 메모리에 db 생성
con = sqlite3.connect(':memory:')

cur = con.cursor()
cur.execute("CREATE TABLE phonebook (name text, phonenum text);")
cur.execute('INSERT INTO phonebook values ("Derick", "010-1234-5678");')
