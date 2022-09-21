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

# Analysis 2: Among all the families with the same-gender-kids,
# how many will have a 3rd kid
cur.execute('SELECT COUNT(*) FROM Fertilities WHERE gender1 = gender2')
num_same_gender_total = cur.fetchone()[0]
cur.execute('''SELECT COUNT(*) FROM Fertilities WHERE gender1 = gender2
    and mkids = ?''', (FM.MKIDS['yes'], ))
num_same_gender_mkids = cur.fetchone()[0]
print('%d families among all same-gender-kids families (%d) have 3rd kid' \
    % (num_same_gender_mkids, num_same_gender_total))

cur.close()

# dump the data into js file
fh = open('gender_mkids.js', 'w')
fh.write("gm_Pie1 = [ ['gender1+gender2', 'number of families'],\n")
fh.write("['male+male', "+str(num_mkids_2m)+"],\n")
fh.write("['female+female', "+str(num_mkids_2f)+"],\n")
fh.write("['other', "+str(num_mkids_all-num_mkids_2m-num_mkids_2f)+"]\n]\n")

fh.write("\n")

fh.write("gm_Pie2 = [ ['more kids', 'number of famllies'], \n")
fh.write("['2 kids', "+str(num_same_gender_total-num_same_gender_mkids)+"],\n")
fh.write("['more than 2 kids', "+str(num_same_gender_mkids)+"]\n]\n")

fh.close()

print("Output written to gender_mkids.js")
print("Open gender_mkids.htm to visualize the data")
