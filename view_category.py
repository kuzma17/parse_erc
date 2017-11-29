#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import os
from function import ErcFunction

print('Status: 200 OK')
print('Content-Type: text/plain')
print('')

form = cgi.FieldStorage()
id = form.getvalue('data')

if id:
    erc = ErcFunction()
    erc.open()
    category = erc.category(id)
    erc.close()
    title = 'Редактирование категории'
    id_val = str(category[0])
    name_val = str(category[1].decode())
else:
    title = 'Создание новой категории'
    id_val = ''
    name_val = ''


print('<h4>'+title+'</h4>')

print('<form method="post" name="category_save" id="category_save" action="category_save.py" >')
print('<input type="hidden" name="id_cat" id="id_cat" value="' + id_val+ '">')

print("""<div class="form-group">
      <label for="name" class="control-label col-sm-2">Название</label>
	  <div class="col-sm-10">""")
print('<input type="text" name="name_cat" id="name_cat" value="' + name_val + '">')
print("""</div>
   </div>
   <div class="form-group">
      <div class="col-sm-offset-2 col-sm-10">""")
print('<button id="edit-submit" type="button" class="btn btn-primary" data-dismiss="modal" value="Save">Сохранить</button>')
print("""</div>
   </div>
   </form>""")