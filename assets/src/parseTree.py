import json
import pandas as pd

with open('../db/dbtree.json', 'r') as f:
    parsed = json.load(f)
parsed = parsed[0:2]
with open('../db/dbtree.json', 'r') as f:
    parsed = json.load(f)
components = {}
for i,p in enumerate(parsed):
	print(i)
	try:
		print(p['27.53E3'])
	except:
		print("no")
	for k,vs in p.items():
		for v in vs:
			try:
				components[v].append(k)
			except:
				components[v] = [k]

print("c",components['27.F6A2'])
maxv = 0
basic = []
df = pd.read_csv('../db/dball.csv')
fontid_map_font = pd.Series(df.楷書字型.values,index=df.字體編號).to_dict()
for k,v in components.items():
	if len(v) > maxv:
		maxv = len(v)
		maxk = k
	if len(v) == 1:
		basic.append(fontid_map_font[k])
print(basic)
print(maxk,maxv)