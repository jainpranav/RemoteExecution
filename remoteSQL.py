#!/usr/bin/python
#-*- coding :utf 8 -*-
# Author : Pranav Jain

r"""
    __________                       __           ___________                            __  .__               
\______   \ ____   _____   _____/  |_  ____   \_   _____/__  ___ ____   ____  __ ___/  |_|__| ____   ____  
 |       _// __ \ /     \ /  _ \   __\/ __ \   |    __)_\  \/  // __ \_/ ___\|  |  \   __\  |/  _ \ /    \ 
 |    |   \  ___/|  Y Y  (  <_> )  | \  ___/   |        \>    <\  ___/\  \___|  |  /|  | |  (  <_> )   |  \
 |____|_  /\___  >__|_|  /\____/|__|  \___  > /_______  /__/\_ \\___  >\___  >____/ |__| |__|\____/|___|  /
        \/     \/      \/                 \/          \/      \/    \/     \/                           \/ 

"""

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
