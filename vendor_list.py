#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from function import ErcFunction
from templates import category_list


erc = ErcFunction()
erc.open()

table = 'erc_vendors'
erc_vendors = erc.cat_list(table)
erc.close()

title = 'Производители'
cat = 'vendor'
category_list(cat, title, erc_vendors)

