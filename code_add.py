#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import code_list

erc = ErcFunction()
erc.open()

print('Status: 200 OK')
print('Content-Type: text/plain')
print('')

form = cgi.FieldStorage()
category = form.getvalue('category')
subcategory = form.getvalue('subcategory')
vendor = form.getvalue('vendor')
code = form.getvalue('code')
parent_code = form.getvalue('parent_code')
title_code = form.getvalue('title')
status = form.getvalue('status')

print(category)
print(subcategory)
print(vendor)
print(code)
print(parent_code)
print(title_code)
print(status)

erc.code_add(category, subcategory, vendor, code, parent_code, title_code, status)
erc.save()

erc_codes = erc.code_list()
erc.close()

title = 'Коды'
cat = 'code'
code_list(cat, title, erc_codes)
