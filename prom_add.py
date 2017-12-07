#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import prom_list

erc = ErcFunction()
erc.open()

form = cgi.FieldStorage()
code = form.getvalue('code')
parent_code = form.getvalue('parent_code')
title_prom = form.getvalue('title_prom')

table = 'erc_promcats'

erc.prom_add(code, parent_code, title_prom)
erc.save()

prom = erc.cat_list(table)
erc.close()

title = 'Prom коды'
cat = 'prom'
prom_list(cat, title, prom)
