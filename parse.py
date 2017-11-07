#!/usr/bin/env python3
import xml.etree.cElementTree as ET
import MySQLdb

fileXML = '/var/www/parse_erc/erc_selected_vendors_20171107_08h29m.xml'

print("Contenr-type:text/html\n\n")

elem = ET.parse(fileXML)
root = elem.getroot()
print(root)
print(len(root))

db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="170270", db="parse_erc", charset='utf8', use_unicode=False)
cursor = db.cursor()
cursor1 = db.cursor()

def add_category(cat):
    sql = "SELECT * FROM erc_sub_categories WHERE name = %s"
    cursor.execute(sql, [cat])
    row = cursor.fetchone()
    #print(row)
    if not row:
        #print('not')
        sql = "INSERT INTO erc_sub_categories (name) VALUES (%s)"
        cursor1.execute(sql, [cat])
        db.commit()


new = ET.Element('new_xml')

for vendor in root.findall('vendor'):
    #name = vendor.get('name')
    #print(name)
    goods = vendor.findall('goods')
    for good in goods:
        print(good[0].text)
        #add_category(good[1].text)



print('End parse.')

db.close()