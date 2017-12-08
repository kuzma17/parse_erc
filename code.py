#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction
from templates import code_view

erc = ErcFunction()
erc.open()

form = cgi.FieldStorage()
id = form.getvalue('data')

table = 'erc_codes'

if id:
    code = erc.code(id)
    title = 'Редактирование кода'
    id_cat = str(code[0])

    category_id = str(code[1])
    subcategory_id = str(code[2])
    vendor_id = str(code[3])
    code_code = code[4]
    status = str(code[5])

else:
    title = 'Создание нового кода'
    id_cat = ''
    category_id = ''
    subcategory_id = ''
    vendor_id = ''
    code_code = ''
    parent_code = ''
    title_code = ''
    status = '0'

code_prom_list = erc.cat_list('erc_promcats')
categories = erc.cat_list('erc_categories')
subcategories = erc.cat_list('erc_subcategories')
vendors = erc.cat_list('erc_vendors')
erc.close()
cat = 'code'
code_view(cat, title, categories, subcategories, vendors, category_id, subcategory_id, vendor_id, id_cat, code_code,code_prom_list, status)
