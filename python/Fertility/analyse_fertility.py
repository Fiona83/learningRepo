"""
This script is used to analyse the fertility data

author: Yerong Chen
date: 2022-09-21
"""

import sqlite3
import re
import fertility_mapper as FM

conn = sqlite3.connect('fertility.sqlite')
cur = conn.cursor()

# Analysis 1: within all families with more than 2 kids
# how many families have first two kids with the same gender
cur.execute('SELECT COUNT(*) FROM Fertilities WHERE mkids = ?', \
    (FM.MKIDS['yes'],))
num_mkids_all = cur.fetchone()[0]

cur.execute('''SELECT COUNT(*) FROM Fertilities
    WHERE mkids = ? and gender1 = ? and gender2 = ?''', \
    (FM.MKIDS['yes'], FM.GENDER['male'], FM.GENDER['male']))
num_mkids_2m = cur.fetchone()[0]

cur.execute('''SELECT COUNT(*) FROM Fertilities
    WHERE mkids = ? and gender1 = ? and gender2 = ?''', \
    (FM.MKIDS['yes'], FM.GENDER['female'],FM.GENDER['female']))
num_mkids_2f = cur.fetchone()[0]

cur.close()

# dump the data into js file
fh = open('gender_mkids.js', 'w')
fh.write("gm_Pie1 = [ ['gender1+gender2', 'number of families'],\n")
fh.write("['male+male', "+str(num_mkids_2m)+"],\n")
fh.write("['female+female', "+str(num_mkids_2f)+"],\n")
fh.write("['other', "+str(num_mkids_all-num_mkids_2m-num_mkids_2f)+"]\n]\n")
fh.close()

print("Output written to gender_mkids.js")
print("Open gender_mkids.htm to visualize the data")
