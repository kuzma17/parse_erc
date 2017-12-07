#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from function import ErcFunction
from templates import prom_list

erc = ErcFunction()
erc.open()

table = 'erc_promcats'

prom = erc.cat_list(table)
erc.close()

title = 'Prom коды'
cat = 'prom'
prom_list(cat, title, prom)

