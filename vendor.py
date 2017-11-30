#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import category_view

form = cgi.FieldStorage()
id = form.getvalue('data')

table = 'erc_vendors'

if id:
    erc = ErcFunction()
    erc.open()
    category = erc.cat(table, id)
    erc.close()
    title = 'Редактирование производителя'
    id_cat = str(category[0])
    name = str(category[1].decode())
else:
    title = 'Создание новой производителя'
    id_cat = ''
    name = ''

cat = 'vendor'
category_view(cat, title, id_cat, name)
