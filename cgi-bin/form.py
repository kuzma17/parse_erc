#!/usr/bin/env python3

import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("currency", "не задано")
text2 = form.getfirst("param1", "не задано")

print("Content-type: text/html\n")
print("<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset='utf-8'>
            <title>Обработка данных форм</title>
        </head>
        <body>")

print("<h1>Обработка данных форм!</h1>")
print("<p>currency: {}</p>".format(text1))
print("<p>param1: {}</p>".format(text2))

print("</body>
</html>")