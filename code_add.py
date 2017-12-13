#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import code_list

erc = ErcFunction()
erc.open()

form = cgi.FieldStorage()
category = form.getvalue('category')
subcategory = form.getvalue('subcategory')
vendor = form.getvalue('vendor')
code = form.getvalue('code_code')
status = form.getvalue('status')


erc.code_add(category, subcategory, vendor, code, status)
erc.save()

erc_codes = erc.code_list()
erc.close()

title = 'Коды'
cat = 'code'
code_list(cat, title, erc_codes)
