import requests
from requests_html import HTMLSession

from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import csv
import pandas as pd

import sys
import os

df = pd.read_csv('./db/db.csv')
imgids = df["字體編號"]
imgmap = [["字體編號","楷書字體編號"]]
for n,id_ in enumerate(imgids):
    print("retrieving img of: ",id_," No. ",n)
    session = HTMLSession()
    r = session.get('http://xiaoxue.iis.sinica.edu.tw/char?fontcode='+id_)
    imgs = r.html.find('img')
    c = 0
    tempmap = []
    for i in imgs:
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
          open('./db/img2/'+i.attrs['alt'][1:-1]+'.png', 'wb').write(r.content)
          #print(i.attrs)
          tempmap.append(i.attrs['alt'][1:-1])
    imgmap.append(tempmap) 
 
with open('./db/dbimg.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(imgmap)
