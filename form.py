#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb
import cgi
import os
import xml.etree.cElementTree as ET
import time

print("Content-type:text/html\n\n")
print("""<html>
    <head>
    </head>
    <body>""")



db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="170270", db="parse_erc", charset='utf8', use_unicode=False)
cursor = db.cursor()
cursor1 = db.cursor()

def catalogs():
    sql = "SELECT * FROM erc_prom_categories"
    cursor.execute(sql)
    return cursor.fetchall()


def categories(category, sub_category, vendor):
    #print(category + ',' + sub_category + ',' + vendor)

    sql = "SELECT pc.code FROM erc_prom_categories AS pc " \
          "LEFT JOIN erc_categories AS ct ON ct.id = pc.category_id " \
          "LEFT JOIN erc_sub_categories AS sc ON sc.id = pc.sub_category_id " \
          "LEFT JOIN erc_vendors AS v ON v.id = pc.vendor_id " \
          "WHERE ct.name = %s AND sc.name = %s AND v.name = %s LIMIT 1"
    #cursor.execute(sql, [category, sub_category, vendor])
    #cursor.execute(sql, [category, sub_category, vendor])
    #cursor.execute(sql)


   # print((str(cursor.fetchone()[0], 'utf-8')))
    #return (str(cursor.fetchone()[0], 'utf-8'))

    # save only is not the data
    sql = "insert into erc_codes (category,sub_category, vendor) " \
          "select %s, %s, %s from dual " \
          "where not exists(select * from erc_codes " \
          "where category = %s and sub_category = %s AND vendor = %s)"
    #cursor.execute(sql, [category, sub_category, vendor, category, sub_category, vendor])

    sql = "SELECT id FROM erc_codes WHERE category = %s and sub_category = %s AND vendor = %s"
    cursor.execute(sql, [category, sub_category, vendor])
    id_code = str(cursor.fetchone()[0])
    print(id_code)

    sql = "SELECT id FROM erc_categories WHERE name = %s"
    cursor.execute(sql, [category])
    id_category = str(cursor.fetchone()[0])
    #print(id_category)

    sql = "SELECT id FROM erc_sub_categories WHERE name = %s"
    cursor.execute(sql, [sub_category])
    id_sub_category = str(cursor.fetchone()[0])
    #print(id_sub_category)

    sql = "SELECT id FROM erc_vendors WHERE name = %s"
    cursor.execute(sql, [vendor])
    id_vendor = str(cursor.fetchone()[0])
    #print(id_vendor)

    sql = "UPDATE erc_codes SET category_id = %s, sub_category_id = %s, vendor_id = %s WHERE id = %s"
    #cursor.execute(sql, [id_category, id_sub_category, id_vendor, id_code])







def prices(ddp, par, sprice, rprice, curr):
    sql = "SELECT a.value FROM erc_arguments AS a LEFT JOIN erc_categories AS ct ON ct.id = a.category_id  WHERE ct.name = %s"
    cursor.execute(sql, [par])
    parr = cursor.fetchone()[0]
    ddp = int(ddp)
    param = float(parr)
    sprice = float(sprice)
    rprice = float(rprice)
    curr = float(curr)
    if ddp == 0:
        currency = curr
    else:
        currency = 1
    price = round(sprice * currency * param, 0)
    price_res = max(price, rprice)
    return str(parr)


dt = time.strftime("%Y-%m-%d %H:%M", time.localtime())
print(dt)

form = cgi.FieldStorage()
text1 = form.getfirst("currency", "не задано")
text2 = form.getfirst("param1", "не задано")
text3 = "123"

print("<strong>Hello CGI </strong><br>")
print(text1 + "<br>")
print(text2 + "<br>")

fileXML = '/var/www/parse_erc/erc_selected_vendors_20171107_08h29m.xml'

#xmlp = ET.XMLParser(encoding="utf-8")
#elem = ET.parse(fileXML, xmlp)
elem = ET.parse(fileXML)
root = elem.getroot()
print(root)
print(len(root))

new = ET.Element('price')
new.set('date', time.strftime("%Y-%m-%d %H:%M", time.localtime()))
name = ET.SubElement(new, 'name')
name.text = 'Интернет-магазин'
currency = ET.SubElement(new, 'currency')
currency.set('code', 'UAH')
currency.text = '7.00'
catalog = ET.SubElement(new, 'catalog')
for cat in catalogs():
    category = ET.SubElement(catalog, 'category')
    category.set('id', str(cat[4], 'utf-8'))
    if str(cat[5], 'utf-8'):
        category.set('parentId', str(cat[5], 'utf-8'))
    category.text = str(cat[6], 'utf-8')

items = ET.SubElement(new, 'items')

for vendor in root.findall('vendor'):
    goods = vendor.findall('goods')
    vendor_name = vendor.get('name')
    for good in goods:
        #print(good[2].text + ' code = ' + good[3].text + '<br>')

        item = ET.SubElement(items, 'item')
        item.set('id', str(good[3].text))
        title = ET.SubElement(item, 'name')
        title.text = good[2].text
        categoryId = ET.SubElement(item, 'categoryId')
        categoryId.text = categories(good[0].text, good[1].text, vendor_name)
        price = ET.SubElement(item, 'price')

        price.text = prices(good[8].text, good[0].text, good[7].text, good[5].text, 1.27)

        image = ET.SubElement(item, 'image')
        image.text = 'http://www.erc.ua/i/goods/' + good[3].text + '.jpg'
        vendor = ET.SubElement(item, 'vendor')
        vendor.text = vendor_name
        description = ET.SubElement(item, 'description')
        description.text = str(good[26].text)
        #if good[27].text:
         #   description.text += str(good[27].text)
        warranty = ET.SubElement(item, 'warranty')
        warranty.text = good[9].text

        country = ET.SubElement(item, 'country')
        country.text = good[24].text

        if good[19].text and str(good[19].text) != '0' and str(good[19].text) != '0.00':
            param_height = ET.SubElement(item, 'param')
            param_height.set('name', 'высота')
            param_height.text = good[19].text

        if good[18].text and str(good[18].text) != '0' and str(good[18].text) != '0.00':
            param_width = ET.SubElement(item, 'param')
            param_width.set('name', 'ширина')
            param_width.text = good[18].text

        if good[20].text and str(good[20].text) != '0' and str(good[20].text) != '0.00':
            param_depth = ET.SubElement(item, 'param')
            param_depth.set('name', 'глубина')
            param_depth.text = good[20].text

        if good[21].text and str(good[21].text) != '0' and str(good[21].text) != '0.00':
            param_weight = ET.SubElement(item, 'param')
            param_weight.set('name', 'вес')
            param_weight.text = good[21].text

        if good[22].text and str(good[22].text) != '0' and str(good[22].text) != '0.00':
            param_volume = ET.SubElement(item, 'param')
            param_volume.set('name', 'объем')
            param_volume.text = good[22].text

db.commit()
db.close()
ET.ElementTree(new).write('/var/www/parse_erc/new.xml', 'utf-8', True)

print('=== New XML Created ===')

print("""</body>
</html>""")
