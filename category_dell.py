#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import category_list

erc = ErcFunction()
erc.open()

form = cgi.FieldStorage()
id_cat = form.getvalue('data')

table = 'erc_categories'

erc.cat_dell(table, id_cat)
erc.save()

categories = erc.cat_list(table)
erc.close()

title = 'Категории'
cat = 'category'
category_list(cat, title, categories)


