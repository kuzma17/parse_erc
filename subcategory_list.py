#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from function import ErcFunction
from templates import category_list


erc = ErcFunction()
erc.open()

table = 'erc_subcategories'
erc_subcategories = erc.cat_list(table)
erc.close()

title = 'Субкатегории'
cat = 'subcategory'
category_list(cat, title, erc_subcategories)

