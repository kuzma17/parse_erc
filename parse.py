#!/usr/bin/env python3
import xml.etree.cElementTree as etree

fileXML = '/var/www/parse_erc/erc_selected_vendors_20171017_04h25m.xml'
tree = etree.parse(fileXML)
root = tree.getroot()
print(root)
print(len(root))

for vendor in root.findall('vendor'):
    goods = vendor.findall('goods')
    for good in goods:
        print(good[2].text + ' code = ' + good[3].text)