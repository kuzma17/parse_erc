#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import category_list

erc = ErcFunction()
erc.open()

form = cgi.FieldStorage()
id_cat = form.getvalue('data')

table = 'erc_subcategories'

erc.cat_dell(table, id_cat)
erc.save()

erc_subcategories = erc.cat_list(table)
erc.close()

title = 'Субкатегории'
cat = 'subcategory'
category_list(cat, title, erc_subcategories)


