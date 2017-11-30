#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from function import ErcFunction
from templates import code_list


erc = ErcFunction()
erc.open()

erc_codes = erc.code_list()
erc.close()

title = 'Коды'
cat = 'code'
code_list(cat, title, erc_codes)

