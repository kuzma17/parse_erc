#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import category_list

erc = ErcFunction()
erc.open()

form = cgi.FieldStorage()
id = form.getvalue('id_cat')
name = form.getvalue('name_cat')

table = 'erc_vendors'

erc.cat_edit(table, id, name)
erc.save()

erc_vendors = erc.cat_list(table)
erc.close()

title = 'Производители'
cat = 'vendor'
category_list(cat, title, erc_vendors)


