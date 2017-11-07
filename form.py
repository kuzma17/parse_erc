#!/usr/bin/env python3
import MySQLdb
import cgi
import os
import xml.etree.cElementTree as ET

print("Content-type:text/html\n\n")
print("""<html>
    <head>
    </head>
    <body>""")

db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="170270", db="parse_erc", charset='utf8', use_unicode=False)
cursor = db.cursor()


def category(title_erc):
    sql = "SELECT category_id, category_title FROM erc_categories WHERE title_erc = %s"
    cursor.execute(sql, [title_erc])
    return cursor.fetchone()


results = category('Багатофункційні лазерні пристрої')
print('category: ')
print(str(results[0], 'utf-8'))
print(' ')
print(str(results[1]))


print('<br>')

#for row in results:
 #   id = row[0]
 #   title_erc = row[1]
 #   id_cat = row[2]
 #   print(title_erc + id_cat)
 #   print("<br>")

db.close()

form = cgi.FieldStorage()
text1 = form.getfirst("currency", "не задано")
text2 = form.getfirst("param1", "не задано")
text3 = "123"

print("<strong>Hello CGI </strong><br>")
print(text1 + "<br>")
print(text2 + "<br>")

fileXML = '/var/www/parse_erc/erc_selected_vendors_20171017_04h25m.xml'

elem = ET.parse(fileXML)
root = elem.getroot()
print(root)
print(len(root))

new = ET.Element('new_xml')

for vendor in root.findall('vendor'):
    goods = vendor.findall('goods')
    for good in goods:
        #print(good[2].text + ' code = ' + good[3].text + '<br>')

        item = ET.SubElement(new, 'item')
        title = ET.SubElement(item, 'title')
        title.text = good[2].text
        code = ET.SubElement(item, 'code')
        code.text = good[3].text
        category = ET.SubElement(item, 'category')
        category.text = good[1].text
        price = ET.SubElement(item, 'price')
        price.text = str(round(float(good[7].text) * 1.025, 2))
        price_r = ET.SubElement(item, 'price_r')
        price_r.text = str(round(float(good[5].text) * 1.075, 2))
        param1 = ET.SubElement(item, 'param')
        param1.set('name', 'высота')
        param1.text = good[19].text
        param2 = ET.SubElement(item, 'param')
        param2.set('name', 'ширина')
        param2.text = good[18].text

ET.ElementTree(new).write('/var/www/parse_erc/new.xml')

print('=== New XML Created ===')

print("""</body>
</html>""")
