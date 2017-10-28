#!/usr/bin/env python3
import cgi
import os
import xml.etree.cElementTree as ET
#import xml.dom.minidom as MN
#from xml.etree import cElementTree



form = cgi.FieldStorage()
text1 = form.getfirst("currency", "не задано")
text2 = form.getfirst("param1", "не задано")
text3 = "123"

print("Contenr-type:text/html\n\n")

print("Hello CGI \n")
print(text1 + "\n")
print(text2 + "\n")

fileXML = '/var/www/html/parse_erc/erc_selected_vendors_20171017_04h25m.xml'

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

ET.ElementTree(new).write('/var/www/html/parse_erc/new.xml')

print('=== New XML Created ===')
