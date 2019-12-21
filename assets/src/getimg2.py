import requests
from requests_html import HTMLSession

from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import json
import pandas as pd

import sys
import os

with open("../db/database_word.json","r") as f:
  db = json.load(f)
imgsown = set(os.listdir('../db/img'))
print(imgsown)

with open('../db/database_word.json','r') as f:
  db = json.load(f)

imgsneedkai = []
imgsneedzhuan = []
for v in db.values():
  imgsneedkai += v['fonts'][0] 
  imgsneedzhuan += v['fonts'][1]
imgsnotownzhuan = []
imgsnotownkai = []
for img in imgsneedkai + imgsneedzhuan:
  if img + '.png' not in imgsown:
    if int(img.split('.')[0]) < 27:
      imgsnotownkai.append(img)
    else:
      imgsnotownzhuan.append(img)
print("needed:",len(imgsneedzhuan),"zhuan fonts")
print("needed:",len(imgsneedkai),"kai fonts")

font_infos = []
print("unowned:",len(imgsnotownzhuan),"zhuan fonts")
print("unowned:",len(imgsnotownkai),"kai fonts")
s()
for n,id_ in enumerate(imgsnotownzhuan):
    print("retrieving img of: ",id_," No. ",n)
    session = HTMLSession()
    r = session.get('http://xiaoxue.iis.sinica.edu.tw/char?fontcode='+id_)
    imgs_html = r.html.find('img')
    temp_info = [i.attrs["alt"][1:-1] for i in imgs_html if "alt" in i.attrs ]
    font_html = r.html.find(' td[style="font-size: 48px"]')
    font = font_html[0].text
    temp_info.append(font)
    print(temp_info)
    font_infos.append(temp_info)
    c = 0
    tempmap = []
    for i in imgs_html:
       #print(i.attrs)
       if "alt" not in i.attrs:
          continue
       img_url = 'http://xiaoxue.iis.sinica.edu.tw'+i.attrs['src']
       # enlarge the picture
       urlinfo = urlparse(img_url)
       #print(urlinfo)
       urlattrs = parse_qs(urlinfo.query)
       #print(urlattrs)
       #urlinfonew= urlencode(urlattrs)
       
       #print(urlinfo)
       urlattrs["size"][0] = '400'
       urlattrsnew= urlencode(urlattrs,doseq=True)
       #print(urlattrs)
       urlinfo = urlinfo._replace(query = urlattrsnew)
       img_url_l = urlunparse(urlinfo)
       
       #print("large: ",img_url_l+'\n')
       #print("small: ",img_url+'\n')
       
       r = requests.get(img_url_l, allow_redirects=True)
       if "alt" in i.attrs:
         open('../db/img/'+i.attrs['alt'][1:-1]+'.png', 'wb').write(r.content)
         #print(i.attrs)
       

s() 
with open('../db/database_font.json', 'r',encoding = "utf8") as f:
    json.dump(font_infos,f)
