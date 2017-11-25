#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
import cgi
import os
import xml.etree.cElementTree as ET
import time


print("Content-type:text/html\n\n")
print("""<html>
    <head>
    </head>
    <body>""")
print('<h2>save categories</h2>')

form = cgi.FieldStorage()
#text1 = form.getfirst("currency", "не задано")

statuses = form.getlist("status")

#print(statuses)
for category in statuses:
    print(category)
    print('<br>')






print("""</body>
</html>""")