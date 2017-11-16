#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb
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


db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="170270", db="parse_erc", charset='utf8', use_unicode=False)
cursor = db.cursor()
cursor1 = db.cursor()

def code_prom(category, sub_category, vendor):
    sql = "SELECT pc.code FROM erc_codes AS pc " \
          "LEFT JOIN erc_categories AS ct ON ct.id = pc.category_id " \
          "LEFT JOIN erc_sub_categories AS sc ON sc.id = pc.sub_category_id " \
          "LEFT JOIN erc_vendors AS v ON v.id = pc.vendor_id " \
          "WHERE ct.name = %s AND sc.name = %s AND v.name = %s LIMIT 1"
    cursor.execute(sql, [category, sub_category, vendor])
    code = cursor.fetchone()[0].decode()

    return code


fileXML = download_patch + filename
#fileXML = '/var/www/parse_erc/erc_selected_vendors_20171107_08h29m.xml'
elem = ET.parse(fileXML)
root = elem.getroot()

print('Status: 200 OK')
print('Content-Type: text/plain')
print('')

tmp_list = []

for vendor in root.findall('vendor'):
    goods = vendor.findall('goods')
    vendor_name = vendor.get('name')
    for good in goods:
        if [vendor_name, good[0].text, good[1].text] in tmp_list:
            continue
        else:
            tmp_list.append([vendor_name, good[0].text, good[1].text])

            code = code_prom(good[0].text, good[1].text, vendor_name)

            if code:
                print('<div class="code_prom" style="color:green; font-family: Geneva, Arial, Helvetica, sans-serif; font-size: 11px; cursor: pointer">')
                print(vendor_name, '=>', good[0].text, '=>', good[1].text, '=>', good[2].text, ' <span class="label label-success" >', code, '</span>')
            else:
                print('<div style="color:red; font-family: Geneva, Arial, Helvetica, sans-serif; font-size: 11px">')
                print(vendor_name, '=>', good[0].text, '=>', good[1].text, '=>', good[2].text, ' <input type="text" name="code["' + good[3].text + '"]">')

            print('</div>')



