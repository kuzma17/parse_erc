#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
from function import ErcFunction

print('Status: 200 OK')
print('Content-Type: text/plain')
print('')

erc = ErcFunction()
erc.open()
currency = erc.currency()
erc.close()

print(currency)
