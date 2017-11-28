#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb
import cgi
import os
import xml.etree.cElementTree as ET
import time

db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="170270", db="parse_erc", charset='utf8', use_unicode=False)
cursor = db.cursor()

print("Content-type:text/html\n\n")
print("""<html>
    <head>
    </head>
    <body>""")


print('34243243243<br>')

print("""</body
</html>""")



