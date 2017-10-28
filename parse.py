#!/usr/bin/env python3
import xml.etree.cElementTree as ET

fileXML = '/var/www/html/parse_erc/erc_selected_vendors_20171017_04h25m.xml'

print("Contenr-type:text/html\n\n")

elem = ET.parse(fileXML)
root = elem.getroot()
print(root)
print(len(root))

new = ET.Element('new_xml')

for vendor in root.findall('vendor'):
    goods = vendor.findall('goods')
    for good in goods:
        print(good[2].text + ' code = ' + good[3].text + '<br>')

        price_text = good[5].text + " === " + str(round(float(good[5].text) * 1.134, 2))

        item = ET.SubElement(new, 'item')
        title = ET.SubElement(item, 'title')
        title.text = good[2].text
        code = ET.SubElement(item, 'code')
        code.text = good[3].text
        category = ET.SubElement(item, 'category')
        category.text = good[1].text
        price = ET.SubElement(item, 'price')
        price.text = price_text

ET.ElementTree(new).write('/var/www/html/parse_erc/new.xml')


print('End parse.')