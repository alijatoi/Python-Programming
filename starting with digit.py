import re
import time
f=open('aasa.txt','r',encoding='utf-8')
mawaad=f.read()
email=re.findall('^[0-9].*',mawaad,re.MULTILINE)
print(email)


time.sleep(10)

