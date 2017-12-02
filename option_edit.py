#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import option_list

erc = ErcFunction()
erc.open()


form = cgi.FieldStorage()
id = form.getvalue('id_cat')
value_cat = form.getvalue('value_cat')
key = form.getvalue('key')

if key == 'currency':
    erc.currency_edit(value_cat)
else:
    erc.option_edit(key, value_cat)

erc.save()

table = 'erc_options'
options = erc.cat_list(table)
erc.close()

title = 'Параметры'
cat = 'option'
option_list(cat, title, options)


