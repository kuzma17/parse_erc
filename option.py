#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import option_view


form = cgi.FieldStorage()
id = form.getvalue('data')

table = 'erc_options'

erc = ErcFunction()
erc.open()
option = erc.cat(table, id)
erc.close()
title = 'Редактирование параметра'
id_cat = str(option[0])
key = str(option[1].decode())
name = str(option[3].decode())
value = str(option[2])

cat = 'option'
option_view(cat, title, id_cat, key, name, value)
