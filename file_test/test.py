#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb
import cgi
import os
import xml.etree.cElementTree as ET
import time

form = cgi.FieldStorage()
currency = form.getvalue('currency')
file_erc = form.getvalue('file_erc')

filename = 'erc.xml'
download_patch = '/var/www/parse_erc/download_file/'

#fn = os.path.basename(filename)
open(download_patch + filename, 'wb').write(file_erc)

print('Status: 200 OK')
print('Content-Type: text/plain')
print('')
print('test_download')
print(currency)