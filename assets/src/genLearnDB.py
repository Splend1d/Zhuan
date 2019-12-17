import json
import os
import pandas as pd
import numpy as np

df = pd.read_csv('../db/database_meaning.txt', sep='\t')
dfimg = pd.read_csv('../db/dbimg.csv')
print(df.columns)
df['字體編號'] = df['字體編號'].str.replace(';', '').str.replace('&', '')
zhuan_map_kai = pd.Series(dfimg.楷書字體編號.values,index=dfimg.字體編號).to_dict()
zhuan_map_def = pd.Series(df.釋義.values,index=df.字體編號).to_dict()
zhuan_map_main = pd.Series(df.部首.values,index=df.字體編號).to_dict()
ks = list(zhuan_map_def.keys())
for k in ks:
	if type(zhuan_map_def[k]) != str:
		del zhuan_map_def[zhuan_map_def[k]]
	if type(zhuan_map_main[k]) != str:
		del zhuan_map_main[zhuan_map_main[k]]
print(len(zhuan_map_def))
with open("../db/dblearn.js","w",encoding = "utf8") as f:
	f.write("var zhuan_map_def =")
	f.write(str(zhuan_map_def))
	f.write(';\n')
	f.write("var zhuan_map_kai =")
	f.write(str(zhuan_map_kai))
	f.write(';\n')
	f.write("var zhuan_map_main =")
	f.write(str(zhuan_map_main))
	f.write(';')
	
