import os 
import pandas as pd
ls = os.listdir("./db/img2")
print(len(ls))
#print(ls)

df = pd.read_csv('./db/db2.csv')
imgids = df["字體編號"]
kimgids = df["楷書字體編號"]
print(len(set(imgids)))
print(len(set(kimgids)))
noimg = []
for img in imgids:
   if img + ".png" not in ls:
      noimg.append(img)
for img in kimgids:
   if img + ".png" not in ls:
      noimg.append(img)
print(noimg)

