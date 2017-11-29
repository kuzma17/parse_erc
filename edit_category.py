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
id = form.getvalue('data')

category = erc.category(id)
erc.close()

print('Редактирование категории<br>')

print('<form method="post" name="category_save" id="category_save" action="category_save.py" >')

print('<input type="hidden" name="id_cat" id="id_cat" value="' + str(category[0]) + '">')

print('<input type="text" name="name_cat" id="name_cat" value="' + str(category[1].decode()) + '">')

print('<button id="edit-submit" type="button" class="btn btn-primary" data-dismiss="modal" value="Save">Save</button>')
print('</form>')