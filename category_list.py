#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from function import ErcFunction
from templates import category_list

erc = ErcFunction()
erc.open()

table = 'erc_categories'

categories = erc.cat_list(table)
erc.close()

title = 'Категории'
cat = 'category'
category_list(cat, title, categories)

