#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import os
import xml.etree.cElementTree as ET
import time
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
    categories = form.getlist("category")
    new_categories = form.getlist("new_category")

    new_vendor = form.getlist("add_vendor")
    new_category = form.getlist("add_category")
    new_subcategory = form.getlist("add_subcategory")
    for category in categories:
        print(category)
        print(' => ')
        status = form.getvalue('status[' + category + ']')
        print(status)
        print('<br>')
        erc.update_status(category, status)

    # print('<hr>')

    for new_id in new_categories:
        print(new_id)
        print(' => ')
        print(new_vendor[int(new_id)])
        print(' : ')
        vendor_id = erc.add_vendor(new_vendor[int(new_id)])
        print(vendor_id)
        print(' => ')
        print(new_category[int(new_id)])
        print(' : ')
        category_id = erc.add_category(new_category[int(new_id)])
        print(category_id)
        print(' => ')
        print(new_subcategory[int(new_id)])
        print(' : ')
        subcategory_id = erc.add_subcategory(new_subcategory[int(new_id)])
        print(subcategory_id)
        print(' => ')
        code = form.getvalue('add_code[' + new_id + ']')
        print(code)
        print(' => ')
        status = form.getvalue('add_status[' + new_id + ']')
        print(status)
        print('<br>')

        if code:
            erc.add_code(vendor_id, category_id, subcategory_id, code, status)
            print('Add str Code<br>')

    erc.save()


fileXML = download_patch + filename
# fileXML = '/var/www/parse_erc/erc_selected_vendors_20171107_08h29m.xml'

try:
    elem = ET.parse(fileXML)
    root = elem.getroot()

    tmp_list = []
    i = 0
    print('<form method="post" name="category_save" id="category_save" action="category_save.py" >')
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
                    print('<input name="status[' + str(
                        int(code[0])) + ']" style="position:absolute; left:-7px; margin-top: 0" type="checkbox" ')
                    if int(code[2]) == 1:
                        print(' checked="checked"')

                    print(' >')
                    print(vendor_name, '=>', good[0].text, '=>', good[1].text, '=>',
                          ' <span class="label label-success" >',
                          code[1].decode(), '</span>')
                    print('<input type="hidden" name="category" value="' + str(int(code[0])) + '" >')

                else:
                    print('<div class="code_prom red">')
                    print('<input name="add_status[' + str(
                        i) + ']" style="position:absolute; left:-7px; margin-top: 0" type="checkbox" >')
                    print(vendor_name, '=>', good[0].text, '=>', good[1].text, '=>',
                          ' <input type="text" name="add_code[' + str(i) + ']">')
                    print('<input type="hidden" name="new_category" value="' + str(i) + '" >')
                    print('<input type="hidden" name="add_vendor" value="' + vendor_name + '" >')
                    print('<input type="hidden" name="add_category" value="' + good[0].text + '" >')
                    print('<input type="hidden" name="add_subcategory" value="' + good[1].text + '" >')
                    i = int(i) + 1

                print('</div>')

    erc.close()

    print(
        '<button id="edit-param" type="button" class="btn btn-primary" data-dismiss="modal" value="Save">Save</button>')
    print('</form>')

    print(
        '<button id="create_xml" type="button" class="btn btn-primary" data-dismiss="modal" value="Create">Create XML file</button>')
except:
    print('<span class="red">Не корректный исходный файл.</span>')
    print('<p>Попробуйте выбрать другой файл.</p>')

