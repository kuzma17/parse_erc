#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import os
import pymysql

db = pymysql.connect(host="127.0.0.1", user="root", passwd="170270", db="parse_erc", charset='utf8', use_unicode=False)
cursor = db.cursor()

def search_1(code):
    sql = "SELECT id FROM erc_codes WHERE code = %s"
    cursor.execute(sql, [code])
    a = cursor.fetchone()[0]
    return a

def add_title(id, parent_id):
    sql = "UPDATE erc_codes SET padern_id = %s WHERE id = %s"
    cursor.execute(sql, [parent_id, id])


print("Content-type:text/html\n\n")
print("""<html>
    <head>
    </head>
    <body>""")

sql = "SELECT id, parent_code FROM erc_codes"
cursor.execute(sql)
arr = cursor.fetchall()

for r in arr:
    print(r[1])

    if r[1] != 0:
        parent_id = search_1(r[1])
        print(parent_id)

    #add_title(r[0].decode(), parent_id)




db.commit()
db.close()
print("""</body
</html>""")



