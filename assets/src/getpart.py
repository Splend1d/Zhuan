import requests
from requests_html import HTMLSession

from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import csv
import pandas as pd

import sys
import os

df = pd.read_csv('./db/db.csv')
df.to_csv('./db/dbparts.csv',index = False)
bins = df["鍵盤字型(binary)"]
parts = []
parts_kai = []
session = HTMLSession()
for n,b in enumerate(bins):
   a = b.split('\\')
   print(n)
   thisbin = 'SearchValue=%'+'%'.join([a[1:3] for a in b.split('\\')[1:]])
   urlformat = ["https://char.iis.sinica.edu.tw/Search2/CharCheck.aspx?","&Ch=%E5%B0%8F%E7%AF%86"]
   urlformat_kai = ["https://char.iis.sinica.edu.tw/Search2/CharCheck.aspx?","&Ch=%e6%a8%99%e6%a5%b7%e9%ab%94"]
   #小篆
   thisurl = thisbin.join(urlformat)
   
   r = session.get(thisurl)
   try:
      thisparts = r.html.find('span')[0].text
      print("zhuan: ",thisparts)
   except:
      thisparts = ""
   parts.append(thisparts)
   #標楷
   thisurl = thisbin.join(urlformat_kai)
   r = session.get(thisurl)
   try:
      thisparts = r.html.find('span')[0].text
      print("kai: ",thisparts)
   except:
      thisparts = ""
   parts_kai.append(thisparts)
with open('./db/dbparts1.txt', 'w') as f:
   for p in parts:
      f.write(p+'\n')
with open('./db/dbparts2.txt', 'w') as f:
   for p in parts_kai:
      f.write(p+'\n')
df["小篆部件"] = parts
df["楷書部件"] = parts_kai
df.to_csv('./db/dbparts.csv',index = False)

   
   
