#!/usr/bin/env python3
import cgi
import os
import xml.etree.cElementTree as CE
#import xml.dom.minidom as MN
#from xml.etree import cElementTree



form = cgi.FieldStorage()
text1 = form.getfirst("currency", "не задано")
text2 = form.getfirst("param1", "не задано")
text3 = "123"

print("Contenr-type:text/html\n\n")


print("Hello CGI \n")
print(text1 + "\n")
print(text2 + "\n")


#with open('/var/www/html/parse_erc/xmlfile.xml', 'rt') as f:
fileXML = '/var/www/html/parse_erc/erc_selected_vendors_20171017_04h25m.xml'
tree = CE.parse(fileXML)

for node in tree.iter(content):
    #print(node[0][0][0])
    print(node.findtext('./gname/Value'))
