#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
import cgi
import os
import xml.etree.cElementTree as ET
import time

form = cgi.FieldStorage()
file_erc = form.getvalue('file_erc')

filename = 'erc.xml'
download_patch = '/var/www/parse_erc/download_file/'

##fn = os.path.basename(filename)
open(download_patch + filename, 'wb').write(file_erc)

db = pymysql.connect(host="127.0.0.1", user="root", passwd="170270", db="parse_erc", charset='utf8', use_unicode=False)
cursor = db.cursor()
cursor1 = db.cursor()


def code_prom(category, sub_category, vendor):
    sql = "SELECT pc.code, pc.status FROM erc_codes AS pc " \
          "LEFT JOIN erc_categories AS ct ON ct.id = pc.category_id " \
          "LEFT JOIN erc_sub_categories AS sc ON sc.id = pc.sub_category_id " \
          "LEFT JOIN erc_vendors AS v ON v.id = pc.vendor_id " \
          "WHERE ct.name = %s AND sc.name = %s AND v.name = %s LIMIT 1"
    cursor.execute(sql, [category, sub_category, vendor])
    code = cursor.fetchone()
    return code


fileXML = download_patch + filename
# fileXML = '/var/www/parse_erc/erc_selected_vendors_20171107_08h29m.xml'
elem = ET.parse(fileXML)
root = elem.getroot()

print('Status: 200 OK')
print('Content-Type: text/plain')
print('')

tmp_list = []

print('<form method="post" name="category_save" id="category_save" action="/cgi-bin/category_save.py" >')
for vendor in root.findall('vendor'):
    goods = vendor.findall('goods')
    vendor_name = vendor.get('name')
    for good in goods:
        if [vendor_name, good[0].text, good[1].text] in tmp_list:
            continue
        else:
            tmp_list.append([vendor_name, good[0].text, good[1].text])

            code = code_prom(good[0].text, good[1].text, vendor_name)

            if code[0]:
                print(
                    '<div class="code_prom" style="color:green; font-family: Geneva, Arial, Helvetica, sans-serif; font-size: 11px; cursor: pointer">')
                print(
                    '<input name="status" style="position:absolute; left:-7px; margin-top: 0" type="checkbox" value="' + str(
                        int(code[0])) + '=' + str(int(code[1])) + '"')
                if int(code[1]) == 1:
                    print(' checked="checked"')

                print(' >')
                print(vendor_name, '=>', good[0].text, '=>', good[1].text, '=>', good[2].text,
                      ' <span class="label label-success" >', code[0].decode(), '</span>')

            else:
                print('<div style="color:red; font-family: Geneva, Arial, Helvetica, sans-serif; font-size: 11px">')
                print('<input name="status" style="position:absolute; left:-7px; margin-top: 0" type="checkbox" >')
                print(vendor_name, '=>', good[0].text, '=>', good[1].text, '=>', good[2].text,
                      ' <input type="text" name="code["' + good[3].text + '"]">')

            print('</div>')

print('<button id="" type="submit" class="btn btn-primary" data-dismiss="modal" value="Save">Save</button>')
print('</form>')



