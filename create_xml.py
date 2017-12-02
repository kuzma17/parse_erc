#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import xml.etree.cElementTree as ET
import time
from function import ErcFunction

erc = ErcFunction()
erc.open()

print('Status: 200 OK')
print('Content-Type: text/plain')
print('')

def prices(ddp, par, sprice, rprice):
    ddp = int(ddp)
    sprice = float(sprice)
    rprice = float(rprice)
    curr = erc.currency()
    param = erc.argument(par)
    if ddp == 0:
        currency = curr
    else:
        currency = 1
    price = round(sprice * currency * param, 0)
    price_out = max(price, rprice)
    return str(price_out)

# Save XML settings
form = cgi.FieldStorage()
erc.save_xml_set(form)
erc.save()

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
    category.set('id', str(cat[4], 'utf-8'))
    if cat[5]:
        category.set('parentId', str(cat[5].decode()))
    category.text = str(cat[6], 'utf-8')

items = ET.SubElement(new, 'items')

for vendor in root.findall('vendor'):
    goods = vendor.findall('goods')
    vendor_name = vendor.get('name')
    for good in goods:
        item_prom = erc.code_prom(good[0].text, good[1].text, vendor_name)
        if item_prom and item_prom[2] == 1 and item_prom[1]:
            item = ET.SubElement(items, 'item')
            item.set('id', str(good[3].text))
            title = ET.SubElement(item, 'name')
            title.text = good[2].text
            categoryId = ET.SubElement(item, 'categoryId')
            categoryId.text = str(item_prom[1].decode())
            price = ET.SubElement(item, 'price')

            price.text = prices(good[8].text, good[0].text, good[7].text, good[5].text)

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

            #country.text = erc.country_ru(good[24].text).decode()

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

ET.ElementTree(new).write('/var/www/parse_erc/file/catalog_prom.xml', 'utf-8', True)

print('<p>XML файл успешно сформирован</p>')
print('<p><a href="/file/catalog_prom.xml" target="_blank"><span class="glyphicon glyphicon-save"></span> скачать</p><br>')
print('<a href="/">Перейти на главную</a>')
