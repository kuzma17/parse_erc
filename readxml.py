#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import xml.etree.cElementTree as ET
from function import ErcFunction

erc = ErcFunction()
erc.open()

print('Status: 200 OK')
print('Content-Type: text/plain')
print('')

form = cgi.FieldStorage()
file_erc = form.getvalue('file_erc')

filename = 'erc.xml'
download_patch = '/var/www/parse_erc/download_file/'

if file_erc:
    open(download_patch + filename, 'wb').write(file_erc)
else:
    erc.save_xml_set(form)
    erc.save()

currency = str(erc.currency())
print('<form method="post" name="category_save" id="category_save" action="category_save.py" >')

print(""" <div class="form-group">
                    <label class="col-md-3 control-label">Курс USD<span class="red">*</span></label>
                    <div class="col-md-9">""")
print('<input type="text" name="currency" id="currency" value="'+currency+'">')
print('</div></div>')

fileXML = download_patch + filename
# fileXML = '/var/www/parse_erc/erc_selected_vendors_20171107_08h29m.xml'

try:
    elem = ET.parse(fileXML)
    root = elem.getroot()

    tmp_list = []
    i = 0

    print('<div class="all_checkbox"><input type="checkbox" id="all_checkbox"> <span id="all_checkbox_text">Выбрать все</span></div>')

    for vendor in root.findall('vendor'):
        goods = vendor.findall('goods')
        vendor_name = vendor.get('name')
        for good in goods:
            if [vendor_name, good[0].text, good[1].text] in tmp_list:
                continue
            else:
                tmp_list.append([vendor_name, good[0].text, good[1].text])

                code = erc.code_prom(good[0].text, good[1].text, vendor_name)

                if code and code[1]:
                    print(
                        '<div class="code_prom green">')
                    print('<div class="block_xml_check"><input name="status[' + str(
                        int(code[0])) + ']" class="xml_check" type="checkbox" ')
                    if int(code[2]) == 1:
                        print(' checked="checked"')

                    print(' ></div>')
                    print(vendor_name, '=>', good[0].text, '=>', good[1].text, '=>',
                          ' <span class="label label-success" >',
                          code[1].decode(), '</span>')
                    print('<input type="hidden" name="category" value="' + str(int(code[0])) + '" >')

                else:
                    print('<div class="code_prom_none red">')
                    print('<input name="add_status[' + str(
                        i) + ']" class="xml_check" type="checkbox" >')
                    print(vendor_name, '=>', good[0].text, '=>', good[1].text, '=>',
                          ' <input type="text" name="add_code[' + str(i) + ']">')
                    print('<input type="hidden" name="new_category" value="' + str(i) + '" >')
                    print('<input type="hidden" name="add_vendor" value="' + vendor_name + '" >')
                    print('<input type="hidden" name="add_category" value="' + good[0].text + '" >')
                    print('<input type="hidden" name="add_subcategory" value="' + good[1].text + '" >')
                    i = int(i) + 1

                print('</div>')

    erc.close()

    print('<div><div class="block_button">')
    print('<button id="edit-param" type="button" class="btn btn-primary" >Записать параметры</button>')
    print('<button id="create_xml" type="button" class="btn btn-success" >Сформировать XML файл</button>')
    print('</div></div>')

except:
    print('<span class="red">Не корректный исходный файл.</span>')
    print('<p>Попробуйте выбрать другой файл.</p><br>')
    print('<a href="/">Перейти на главную</a>')

print('</form>')

