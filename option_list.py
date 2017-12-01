#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from function import ErcFunction
from templates import option_list

erc = ErcFunction()
erc.open()

table = 'erc_options'

options = erc.cat_list(table)
erc.close()

title = 'Параметры'
cat = 'option'
option_list(cat, title, options)

