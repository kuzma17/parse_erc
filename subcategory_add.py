#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import category_list

erc = ErcFunction()
erc.open()

form = cgi.FieldStorage()
name = form.getvalue('name_cat')

table = 'erc_sub_categories'
erc.cat_add(table, name)
erc.save()

erc_sub_categories = erc.cat_list(table)
erc.close()

title = 'Субкатегории'
cat = 'subcategory'
category_list(cat, title, erc_sub_categories)
