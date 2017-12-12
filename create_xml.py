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
currencies = ET.SubElement(new, 'currencies')
currency = ET.SubElement(currencies, 'currency')
currency.set('id', 'USD')
currency.set('rate', 'CB')
currency = ET.SubElement(currencies, 'currency')
currency.set('id', 'KZT')
currency.set('rate', 'CB')
currency = ET.SubElement(currencies, 'currency')
currency.set('id', 'RUR')
currency.set('rate', 'CB')
currency = ET.SubElement(currencies, 'currency')
currency.set('id', 'BYN')
currency.set('rate', 'CB')
currency = ET.SubElement(currencies, 'currency')
currency.set('id', 'UAH')
currency.set('rate', '1')
currency = ET.SubElement(currencies, 'currency')
currency.set('id', 'EUR')
currency.set('rate', 'CB')
catalog = ET.SubElement(new, 'catalog')
for cat in erc.catalogs():
    category = ET.SubElement(catalog, 'category')
    category.set('id', str(cat[1]))
    if int(cat[2]) != 0:
        category.set('parentId', str(cat[2]))
    category.text = str(cat[3], 'utf-8')

offers = ET.SubElement(new, 'offers')

for vendor in root.findall('vendor'):
    goods = vendor.findall('goods')
    vendor_name = vendor.get('name')
    for good in goods:
        item_prom = erc.code_prom(good[0].text, good[1].text, vendor_name)
        if item_prom and item_prom[2] == 1 and item_prom[1]:
            offer = ET.SubElement(offers, 'offer')
            if str(good[11].text) == 'Да':
                available_text = 'true'
            else:
                available_text = ''
            offer.set('available', available_text)
            offer.set('id', good[3].text)
            offer.set('selling_type', 'r')
            price = ET.SubElement(offer, 'price')
            price.text = prices(good[8].text, good[0].text, good[7].text, good[5].text)
            categoryId = ET.SubElement(offer, 'categoryId')
            categoryId.text = str(item_prom[1])
            picture = ET.SubElement(offer, 'picture')
            picture.text = 'http://www.erc.ua/i/goods/' + good[3].text + '.jpg'
            currencyId = ET.SubElement(offer, 'currencyId')
            currencyId.text = 'UAH'
            pickup = ET.SubElement(offer, 'pickup')
            pickup.text = 'true'
            delivery = ET.SubElement(offer, 'delivery')
            delivery.text = 'true'
            name = ET.SubElement(offer, 'name')
            name.text = good[2].text
            vendor = ET.SubElement(offer, 'vendor')
            vendor.text = str(erc.vendor_prom(vendor_name).decode())
            vendorCode = ET.SubElement(offer, 'vendorCode')
            vendorCode.text = good[3].text
            #country_of_origin = ET.SubElement(offer, 'country_of_origin')
            if good[24].text:
                country_of_origin = ET.SubElement(offer, 'country_of_origin')
                country_text = erc.country_ru(good[24].text).decode()

            country_of_origin.text = country_text
            description = ET.SubElement(offer, 'description')
            description.text = '<![CDATA[' + str(good[26].text) + ']]>'
            sales_notes = ET.SubElement(offer, 'sales_notes')
            sales_notes.text = 'предоплата'

            if good[20].text and str(good[20].text) != '0' and str(good[20].text) != '0.00':
                param_height = ET.SubElement(offer, 'param')
                param_height.set('name', 'Высота')
                param_height.set('unit', 'см')
                param_height.text = good[20].text

            if good[19].text and str(good[19].text) != '0' and str(good[19].text) != '0.00':
                param_width = ET.SubElement(offer, 'param')
                param_width.set('name', 'Ширина')
                param_width.set('unit', 'см')
                param_width.text = good[19].text

            if good[21].text and str(good[21].text) != '0' and str(good[21].text) != '0.00':
                param_depth = ET.SubElement(offer, 'param')
                param_depth.set('name', 'Глубина')
                param_depth.set('unit', 'см')
                param_depth.text = good[21].text

            if good[22].text and str(good[22].text) != '0' and str(good[22].text) != '0.00':
                param_weight = ET.SubElement(offer, 'param')
                param_weight.set('name', 'Вес')
                param_weight.set('unit', 'кг')
                param_weight.text = good[22].text

            if good[23].text and str(good[23].text) != '0' and str(good[23].text) != '0.00':
                param_volume = ET.SubElement(offer, 'param')
                param_volume.set('name', 'Объем')
                param_volume.set('unit', '(кв.м.)')
                param_volume.text = good[23].text

            if good[9].text and str(good[9].text) != '0' and str(good[9].text) != '0.00':
                param_warranty = ET.SubElement(offer, 'param')
                param_warranty.set('name', 'Гарантия')
                param_warranty.set('unit', good[10].text)
                if int(good[9].text) > 0:
                    param_warranty_text = good[9].text
                else:
                    param_warranty_text = '0'
                param_warranty.text = param_warranty_text

erc.close()

ET.ElementTree(new).write('/var/www/parse_erc/file/catalog_prom.xml', 'utf-8', True)

print('<p>XML файл успешно сформирован</p>')
print('<p><a href="/file/catalog_prom.xml" target="_blank"><span class="glyphicon glyphicon-save"></span> скачать</p><br>')
print('<a href="/">Перейти на главную</a>')
