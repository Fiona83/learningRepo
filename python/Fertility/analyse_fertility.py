"""
This script is used to analyse the fertility data

author: Yerong Chen
date: 2022-09-21
"""

import sqlite3

conn = sqlite3.connect('fertility.sqlite')
cur = conn.cursor()
