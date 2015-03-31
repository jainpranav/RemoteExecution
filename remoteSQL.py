#!/usr/bin/python
#-*- coding :utf 8 -*-
# Author : Pranav Jain

import MySQLdb
import prettytable

from prettytable import from_db_cursor

host = str(raw_input('Kindly Enter Host Name '))
user = str(raw_input('Kindly Enter your username '))
passwd = str(raw_input('Kindly Enter your  password '))

database = str(raw_input('Kindly Enter the Database '))

db = MySQLdb.connect(host, # your host, usually localhost 
                    user, # your username
                    passwd, # your password
                    database) # name of the database)



cur = db.cursor() 

column = raw_input('Kindly Enter Column Name')
table = raw_input('Kindly Enter Table name')

#columns = map(col, col.split())

cur.execute("SELECT "+column+" FROM "+database+ "."+table+"")
pt = from_db_cursor(cur)

print pt
cur.close()
