import re
print(re.search(r'\d',"fda12hellowo231rld"))

print(re.search(r"[0,1]\d\d|2[0-4]\d|25[0-5]",'200'))

print(re.search(r'((([0,1]{0,1}\d{0,1}\d|2{0,1}[0-4]{0,1}\d|2{0,1}5{0,1}[0-5])\.){3}([0,1]{0,1}\d{0,1}\d|2{0,1}[0-4]{0,1}\d|2{0,1}5{0,1}[0-5]))','198.10.23.2'))

print(re.search(r'<.+>','<html><title>hello</title></html>'))

print(re.search(r'<.+?>','<html><title>hello</title></html>'))
