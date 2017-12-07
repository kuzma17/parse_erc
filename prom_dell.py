#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import prom_list

erc = ErcFunction()
erc.open()

form = cgi.FieldStorage()
id_cat = form.getvalue('data')

table = 'erc_promcats'

erc.cat_dell(table, id_cat)
erc.save()


prom = erc.cat_list(table)
erc.close()

title = 'Prom коды'
cat = 'prom'
prom_list(cat, title, prom)


