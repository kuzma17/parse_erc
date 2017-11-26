#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
import cgi
import os
import xml.etree.cElementTree as ET
import time

db = pymysql.connect(host="127.0.0.1", user="root", passwd="170270", db="parse_erc", charset='utf8', use_unicode=False)
cursor = db.cursor()

def update_status(id, status):
    if status == 'on':
        status = 1
    else:
        status = 0

    sql = "UPDATE erc_codes SET status = %s WHERE id = %s"
    cursor.execute(sql, [status, id])

def add_vendor(vendor):
    sql = "SELECT id FROM erc_vendors WHERE name = %s"
    cursor.execute(sql, [vendor])
    id = cursor.fetchone()[0]
    return id

def add_category(name):
    sql = "SELECT id FROM erc_categories WHERE name = %s"
    cursor.execute(sql, [name])
    id = cursor.fetchone()[0]
    return id

def add_subcategory(name):
    sql = "SELECT id FROM erc_sub_categories WHERE name = %s"
    cursor.execute(sql, [name])
    id = cursor.fetchone()[0]
    return id



print("Content-type:text/html\n\n")
print("""<html>
    <head>
    </head>
    <body>""")
print('<h2>save categories</h2>')

form = cgi.FieldStorage()
#text1 = form.getfirst("currency", "не задано")

categories = form.getlist("category")
new_categories = form.getlist("new_category")

new_vendor = form.getlist("add_vendor")
new_category = form.getlist("add_category")
new_subcategory = form.getlist("add_subcategory")

for category in categories:
    print(category)
    print(' => ')
    status = form.getvalue('status['+category+']')
    print(status)
    print('<br>')
    update_status(category, status)

print('<hr>')

for new_id in new_categories:
    print(new_id)
    print(' => ')
    print(new_vendor[int(new_id)])
    print(' : ')
    print(add_vendor(new_vendor[int(new_id)]))
    print(' => ')
    print(new_category[int(new_id)])
    print(' : ')
    print(add_category(new_category[int(new_id)]))
    print(' => ')
    print(new_subcategory[int(new_id)])
    print(' : ')
    print(add_subcategory(new_subcategory[int(new_id)]))
    print(' => ')
    print(form.getvalue('add_code['+new_id+']'))
    print(' => ')
    print(form.getvalue('add_status['+new_id+']'))
    print('<br>')


db.commit()
db.close()

print("""</body>
</html>""")