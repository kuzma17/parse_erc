#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import os
import xml.etree.cElementTree as ET
import time
from function import ErcFunction

erc = ErcFunction()
erc.open()

print("Content-type:text/html\n\n")
print("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <meta charset="utf-8">
    <link href="/css/style.css" rel="stylesheet"/>
    <link rel="stylesheet" href="/css/bootstrap.min.css" >
    <link rel="stylesheet" href=/"css/font-awesome.min.css">
    <script type="text/javascript" src="/js/jquery.min.js"></script>
</head>
<body style="background-color: #e0ebeb;">""")
print('<h2>Created erc xml</h2>')

filename = 'erc.xml'
download_patch = '/var/www/parse_erc/download_file/'

fileXML = download_patch + filename

dt = time.strftime("%Y-%m-%d %H:%M", time.localtime())

elem = ET.parse(fileXML)
root = elem.getroot()
new = ET.Element('price')
new.set('date', time.strftime("%Y-%m-%d %H:%M", time.localtime()))
name = ET.SubElement(new, 'name')
name.text = 'Интернет-магазин'
currency = ET.SubElement(new, 'currency')
currency.set('code', 'UAH')
currency.text = '7.00'
catalog = ET.SubElement(new, 'catalog')
for cat in erc.catalogs():
    category = ET.SubElement(catalog, 'category')
    category.set('id', str(cat[8], 'utf-8'))
    if cat[9]:
        category.set('parentId', str(cat[9]))
    category.text = str(cat[10], 'utf-8')

items = ET.SubElement(new, 'items')

for vendor in root.findall('vendor'):
    goods = vendor.findall('goods')
    vendor_name = vendor.get('name')
    for good in goods:
        item_prom = erc.code_prom(good[0].text, good[1].text, vendor_name)
        if item_prom[2] == 1 and item_prom[1]:
            item = ET.SubElement(items, 'item')
            item.set('id', str(good[3].text))
            title = ET.SubElement(item, 'name')
            title.text = good[2].text
            categoryId = ET.SubElement(item, 'categoryId')
            categoryId.text = str(item_prom[1].decode())
            price = ET.SubElement(item, 'price')

            price.text = erc.prices(good[8].text, good[0].text, good[7].text, good[5].text, 1.27)

            image = ET.SubElement(item, 'image')
            image.text = 'http://www.erc.ua/i/goods/' + good[3].text + '.jpg'
            vendor = ET.SubElement(item, 'vendor')
            vendor.text = vendor_name
            description = ET.SubElement(item, 'description')
            description.text = str(good[26].text)
            # if good[27].text:
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

erc.close()

ET.ElementTree(new).write('/var/www/parse_erc/new.xml', 'utf-8', True)

print('=== New XML Created ===')

print("""</body>
</html>""")