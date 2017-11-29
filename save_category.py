#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import os
from function import ErcFunction

erc = ErcFunction()
erc.open()

print('Status: 200 OK')
print('Content-Type: text/plain')
print('')

form = cgi.FieldStorage()
id = form.getvalue('id_cat')
name = form.getvalue('name_cat')

erc.edit_category(id, name)
erc.save()

categories = erc.categories()
erc.close()

print("""<table class="" cellpadding="1" cellspacing="1" border="1">
                <tr>
                    <th>id</th><th>name</th><th></th>
                </tr>""")
for category in categories:
    print('<tr>')
    print('<td>' + str(category[0]) + '</td>')
    print('<td>' + str(category[1].decode()) + '</td>')
    print('<td><a class="edit_category" data-id="'+str(category[0])+'" href="#">edit</a> <a href="#">del</a></td>')
    print('</tr>')
print('<table>')

