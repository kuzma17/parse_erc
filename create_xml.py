#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import time
import re
import xml.etree.cElementTree as ET
from function import ErcFunction
from xml.dom import minidom

erc = ErcFunction()
erc.open()

print('Status: 200 OK')
print('Content-Type: text-plain')
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

doc = minidom.Document()
price = doc.createElement('price')

doc.appendChild(price)
price.setAttribute('date', time.strftime("%Y-%m-%d %H:%M", time.localtime()))

name = doc.createElement('name')
price.appendChild(name)
text = doc.createTextNode('Интернет-магазин')
name.appendChild(text)

currencies = doc.createElement('currencies')
price.appendChild(currencies)
currency_usd = doc.createElement('currency')
currencies.appendChild(currency_usd)
currency_usd.setAttribute('id', 'USD')
currency_usd.setAttribute('rate', 'CB')
currency_kzt = doc.createElement('currency')
currencies.appendChild(currency_kzt)
currency_kzt.setAttribute('id', 'KZT')
currency_kzt.setAttribute('rate', 'CB')
currency_rur = doc.createElement('currency')
currencies.appendChild(currency_rur)
currency_rur.setAttribute('id', 'RUR')
currency_rur.setAttribute('rate', 'CB')
currency_byn = doc.createElement('currency')
currencies.appendChild(currency_byn)
currency_byn.setAttribute('id', 'BYN')
currency_byn.setAttribute('rate', 'CB')
currency_uah = doc.createElement('currency')
currencies.appendChild(currency_uah)
currency_uah.setAttribute('id', 'UAH')
currency_uah.setAttribute('rate', 'CB')
currency_eur = doc.createElement('currency')
currencies.appendChild(currency_eur)
currency_eur.setAttribute('id', 'EUR')
currency_eur.setAttribute('rate', 'CB')

catalog = doc.createElement('catalog')
price.appendChild(catalog)

for cat in erc.catalogs():
    category = doc.createElement('category')
    catalog.appendChild(category)
    category.setAttribute('id', str(cat[1]))
    if int(cat[2]) != 0:
        category.setAttribute('parentId', str(cat[2]))
    text = doc.createTextNode(str(cat[3], 'utf-8'))
    category.appendChild(text)

offers = doc.createElement('offers')
price.appendChild(offers)

for vendor in root.findall('vendor'):
    goods = vendor.findall('goods')
    vendor_name = vendor.get('name')
    for good in goods:
        item_prom = erc.code_prom(good[0].text, good[1].text, vendor_name)
        if item_prom and item_prom[2] == 1 and item_prom[1]:
            offer = doc.createElement('offer')
            offers.appendChild(offer)
            if str(good[11].text) == 'Есть':
                available_text = 'true'
            else:
                available_text = ''
            offer.setAttribute('available', available_text)
            offer.setAttribute('id', good[3].text)
            offer.setAttribute('selling_type', 'r')

            price = doc.createElement('price')
            offer.appendChild(price)
            text = doc.createTextNode(prices(good[8].text, good[0].text, good[7].text, good[5].text))
            price.appendChild(text)

            categoryId = doc.createElement('categoryId')
            offer.appendChild(categoryId)
            text = doc.createTextNode(str(item_prom[1]))
            categoryId.appendChild(text)

            picture = doc.createElement('picture')
            offer.appendChild(picture)
            text = doc.createTextNode('http://www.erc.ua/i/goods/' + good[3].text + '.jpg')
            picture.appendChild(text)

            currencyId = doc.createElement('currencyId')
            offer.appendChild(currencyId)
            text = doc.createTextNode('UAH')
            currencyId.appendChild(text)

            pickup = doc.createElement('pickup')
            offer.appendChild(pickup)
            text = doc.createTextNode('true')
            pickup.appendChild(text)

            delivery = doc.createElement('delivery')
            offer.appendChild(delivery)
            text = doc.createTextNode('true')
            delivery.appendChild(text)

            name = doc.createElement('name')
            offer.appendChild(name)
            text = doc.createTextNode(good[2].text)
            name.appendChild(text)

            vendor = doc.createElement('vendor')
            offer.appendChild(vendor)
            text = doc.createTextNode(str(erc.vendor_prom(vendor_name).decode()))
            vendor.appendChild(text)

            vendorCode = doc.createElement('vendorCode')
            offer.appendChild(vendorCode)
            text = doc.createTextNode(good[3].text)
            vendorCode.appendChild(text)

            if good[24].text:
                country_of_origin = doc.createElement('country_of_origin')
                offer.appendChild(country_of_origin)
                text = doc.createTextNode(good[24].text)
                country_of_origin.appendChild(text)

            description = doc.createElement('description')
            offer.appendChild(description)
            cdata = doc.createCDATASection(str(good[26].text))
            description.appendChild(cdata)

            sales_notes = doc.createElement('sales_notes')
            offer.appendChild(sales_notes)
            text = doc.createTextNode('предоплата')
            sales_notes.appendChild(text)

            if good[20].text and str(good[20].text) != '0' and str(good[20].text) != '0.00':
                param_height = doc.createElement('param')
                offer.appendChild(param_height)
                param_height.setAttribute('name', 'Высота')
                param_height.setAttribute('unit', 'см')
                text = doc.createTextNode(good[20].text)
                param_height.appendChild(text)

            if good[19].text and str(good[19].text) != '0' and str(good[19].text) != '0.00':
                param_width = doc.createElement('param')
                offer.appendChild(param_width)
                param_width.setAttribute('name', 'Ширина')
                param_width.setAttribute('unit', 'см')
                text = doc.createTextNode(good[19].text)
                param_width.appendChild(text)

            if good[21].text and str(good[21].text) != '0' and str(good[21].text) != '0.00':
                param_depth = doc.createElement('param')
                offer.appendChild(param_depth)
                param_depth.setAttribute('name', 'Глубина')
                param_depth.setAttribute('unit', 'см')
                text = doc.createTextNode(good[21].text)
                param_depth.appendChild(text)

            if good[22].text and str(good[22].text) != '0' and str(good[22].text) != '0.00':
                param_weight = doc.createElement('param')
                offer.appendChild(param_weight)
                param_weight.setAttribute('name', 'Вес')
                param_weight.setAttribute('unit', 'кг')
                text = doc.createTextNode(good[22].text)
                param_weight.appendChild(text)

            if good[23].text and str(good[23].text) != '0' and str(good[23].text) != '0.00':
                param_volume = doc.createElement('param')
                offer.appendChild(param_volume)
                param_volume.setAttribute('name', 'Объем')
                param_volume.setAttribute('unit', '(кв.м.)')
                text = doc.createTextNode(good[23].text)
                param_volume.appendChild(text)

            if good[9].text and str(good[9].text) != '0' and str(good[9].text) != '0.00':
                param_warranty = doc.createElement('param')
                offer.appendChild(param_warranty)
                param_warranty.setAttribute('name', 'Гарантия')
                param_warranty.setAttribute('unit', good[10].text)
                if int(good[9].text) > 0:
                    text = doc.createTextNode(good[9].text)
                else:
                    text = doc.createTextNode('0')
                param_warranty.appendChild(text)
erc.close()

xml_str = doc.toprettyxml()

xml_str = re.sub(r'\n+', '\n', xml_str)
#xml_str = re.sub(r'\s+', ' ', xml_str)

with open("/var/www/parse_erc/file/catalog_prom.xml", "w", encoding="utf8") as f:
    f.write(xml_str)

print('<p>XML файл успешно сформирован</p>')
print('<p><a href="/file/catalog_prom.xml" target="_blank"><span class="glyphicon glyphicon-save"></span> скачать</p><br>')
print('<a href="/">Перейти на главную</a>')
