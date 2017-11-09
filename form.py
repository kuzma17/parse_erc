#!/usr/bin/env python3
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


def category(category, sub_category, vendor):
    cat = sub_category
    #sql = "SELECT category_id, category_title FROM erc_categories WHERE title_erc = %s"
    #cursor.execute(sql, [title_erc])
    return str('TR432432')

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
    return str(price_res)


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

elem = ET.parse(fileXML)
root = elem.getroot()
print(root)
print(len(root))

new = ET.Element('price')
new.set('date', time.strftime("%Y-%m-%d %H:%M", time.localtime()))
name = ET.SubElement(new, 'name')
name.text = 'Интернет-магазин'
currency = ET.SubElement(new, 'currency')
currency.set('code', 'USD')
currency.text = '7.00'
catalog = ET.SubElement(new, 'catalog')

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
        categoryId.text = category(good[0].text, good[1].text, vendor_name)
        price = ET.SubElement(item, 'price')
        price.text = prices(good[8].text, good[0].text, good[7].text, good[5].text, text1)
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


db.close()
ET.ElementTree(new).write('/var/www/parse_erc/new.xml')

print('=== New XML Created ===')

print("""</body>
</html>""")
