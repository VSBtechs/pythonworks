#Code for some challenges :)
#challenge00
p=2**38 #put this value of p in the given link at last 
#challenge01
t='g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj'
key='abcdefghijklmnopqrstuvwxyz' #by ceaser cipher
result=''
for l in t:
 if l in key:
  i = (key.index(l) + 2) % 26
  result += key[i]
 else :
  result += l

print(result)
#challenge02
import re,os
p=re.compile(r'[a-z]')
ocr=open('/home/virat/Desktop/Untitled Folder 8/python/pch/ocr.txt')#contains sourcepage commented text
ocrcont=ocr.read()

r=p.findall(ocrcont)
print(r)

ocr.close()
#challenge03
import re,os
p=re.compile(r'[^A-Z][A-Z]{3}?([a-z]{1}?)[A-Z]{3}[^A-Z]')
re=open('/home/virat/Desktop/Untitled Folder 8/python/pch/re.txt')#contains sourcepage commented text
recont=re.read()
r=p.findall(recont)
print(r)
re.close()
