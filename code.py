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
    code = erc.cat(table, id)
    title = 'Редактирование кода'
    id_cat = str(code[0])

    category_id = str(code[1])
    subcategory_id = str(code[2])
    vendor_id = str(code[3])
    code_code = str(code[4].decode())
    parent_code = str(code[5].decode())
    title_code = str(code[6].decode())
    status = str(code[7])

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

categories = erc.cat_list('erc_categories')
subcategories = erc.cat_list('erc_sub_categories')
vendors = erc.cat_list('erc_vendors')
erc.close()
cat = 'code'
code_view(cat, title, categories, subcategories, vendors, category_id, subcategory_id, vendor_id, id_cat, code_code, parent_code, title_code, status)
