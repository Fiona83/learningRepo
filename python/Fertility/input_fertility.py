"""
This file is used to read data from the fertility file
and import it into a database for further analyse

Structure of the database
1. Ethnicities (id integer primary key, eth text unique)
2. Fertilities (id integer primary key, mkids integer,
    gender1 integer, gender2 interger, age interger,
    work_hrs interger, eth_id interger)
    mkids: 0 = no, 1 = yes
    gender: 0 = male, 1 = female

author: Yerong Chen
data: 2022-09-20
"""

import sqlite3
import fertility_mapper as FM


# create database
conn = sqlite3.connect('fertility.sqlite')
cur = conn.cursor()

mkids_mapper = FM.MKIDS
gender_mapper = FM.GENDER


# create the table of Ethnicities
eth_mapper = {'Caucasian':1, 'African-American':2, 'Hispanic':3, 'Other':4}
cur.executescript('''
    DROP TABLE IF EXISTS Ethnicities;

    CREATE TABLE Ethnicities (
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    eth TEXT NOT NULL UNIQUE
    )
''')
for (eth, eval) in eth_mapper.items():
    cur.execute('''INSERT OR IGNORE INTO Ethnicities (id, eth)
        VALUES (?, ?)''', (eval, eth))

def get_eth_id (afam, hisp, other):
    if afam == 'yes':
        if hisp == 'yes' or other == 'yes':
            eth = -1
        else:
            eth = eth_mapper['African-American']
    elif hisp == 'yes':
        if afam == 'yes' or other == 'yes':
            eth = -1
        else:
            eth = eth_mapper['Hispanic']
    elif other == 'yes':
        if afam == 'yes' or hisp == 'yes':
            eth = -1
        else: eth = eth_mapper['Other']
    else:
        eth = eth_mapper['Caucasian']

    return eth

# create the table Fertilities
cur.execute('''
    CREATE TABLE IF NOT EXISTS Fertilities (
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    mkids INTEGER NOT NULL,
    gender1 INTEGER NOT NULL,
    gender2 INTEGER NOT NULL,
    age INTEGER,
    work_hrs INTEGER,
    eth_id INTEGER NOT NULL
    )
''')

conn.commit()

# open the file
fname = "Fertility2.csv"
try:
    fh = open(fname)
except Exception as err:
    print("Cannot open the file:", fname)
    print(err)
    quit()

c_insert = 0
c_update = 0
for line in fh:
    line = line.strip()
    pieces = line.split(',')
    #print(pieces)
    id = pieces[0][1:-1]
    if not id: continue
    mkkey = pieces[1][1:-1]
    mkids = mkids_mapper[mkkey]
    g1key = pieces[2][1:-1]
    g1 = gender_mapper[g1key]
    g2key = pieces[3][1:-1]
    g2 = gender_mapper[g2key]
    age = int(pieces[4])
    work_hrs = int(pieces[8])
    eth = get_eth_id(pieces[5][1:-1], pieces[6][1:-1], pieces[7][1:-1])
    #print(id, mkids, g1, g2, age, work_hrs, eth)
    #break

    # check if this id is already in the database
    cur.execute('SELECT id FROM Fertilities WHERE id = ?', (id,))
    row = cur.fetchone()
    if row is None:
        cur.execute(''' INSERT INTO Fertilities (mkids, gender1, gender2,
        age, work_hrs, eth_id) VALUES (?,?,?,?,?,?)''', (mkids, g1, g2, \
        age, work_hrs, eth))
        c_insert += 1
    else:
        cur.execute(''' UPDATE Fertilities SET mkids = ?,gender1 = ?,
        gender2 = ?, age = ?, work_hrs = ?, eth_id = ? WHERE id = ?''', \
        (mkids, g1, g2, age, work_hrs, eth, id))
        c_update += 1

    conn.commit()

cur.close()
print('%d rows are inserted and %d rows are updated.' % (c_insert, c_update))
