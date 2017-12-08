#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import prom_view

form = cgi.FieldStorage()
id = form.getvalue('data')
table = 'erc_promcats'

erc = ErcFunction()
erc.open()

if id:
    prom = erc.cat(table, id)
    title = 'Редактирование Prom кода'
    id_cat = str(prom[0])
    code = str(prom[1])
    parent_code = prom[2]
    title_code = str(prom[3].decode())
else:
    title = 'Создание нового Prom кода'
    id_cat = ''
    code = ''
    parent_code = ''
    title_code = ''

cat = 'prom'
list_code = erc.prom_list()
erc.close()
prom_view(cat, title, id_cat, code, parent_code, title_code, list_code)
