#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import os
from function import ErcFunction

erc = ErcFunction()
erc.open()

categories = erc.categories()
erc.close()

print('Status: 200 OK')
print('Content-Type: text/plain')
print('')

print('<button id="add_category" type="button" class="btn btn-default">Добавить</button><br>')
print("""<table class="table table-hover white_bg">
            <thead>
                <tr>
                    <th>id</th><th>name</th><th></th>
                </tr>
            <thead>""")
for category in categories:
    print('<tr>')
    print('<td>' + str(category[0]) + '</td>')
    print('<td>' + str(category[1].decode()) + '</td>')
    print('<td><a class="edit_category" data-id="'+str(category[0])+'" href="#"><span class="glyphicon glyphicon-edit green"></span></a> <a class="dell_category" data-id="'+str(category[0])+'" href="#"><span class="glyphicon glyphicon-remove red"></span></a></td>')
    print('</tr>')
print('<table>')
