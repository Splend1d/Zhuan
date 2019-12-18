import json
import pandas as pd
with open('../db/dbtree.json', 'r') as f:
    parsed = json.load(f)
components = {}

df = pd.read_csv('../db/dball.csv')
fontid_map_font = pd.Series(df.楷書字型.values, index=df.字體編號).to_dict()  # for human eye evaluation
p = parsed[0]
zhuan_map_parent = parsed[0]
for k, vs in p.items():
    for v in vs:
        try:
            components[v].append(k)
        except:
            components[v] = [k]
basic = []
maxv = 0
for k, v in components.items():
    if len(v) == 1:
        basic.append(k)
print(basic)

for i, p in enumerate(parsed[1:]):
    print(i)
    try:
        print(p['27.53E3'])
    except:
        print("no")
    for k, vs in p.items():
        for v in vs:
            # print(v)
            # print(basic)
            if k in basic:
                try:
                    components[v].append(k)
                except:
                    stop()  # this should never happen
                    components[v] = [k]
                # print(components[v])
                # print(k, v)
for k in components:
    components[k] = sorted(components[k])
print(components["27.8FA8"])
zhuan_map_child = components
print("c", components['27.8FA8'])


# a basic character is of rank 1
# two basic characters is rank 2
#

# for k,v in components.items():
# 	if len(v) > maxv:
# 		maxv = len(v)
# 		maxk = k
# 	if len(v) == 1:
# 		basic.append(fontid_map_font[k])
# print(basic)
# print(maxk,maxv)

with open("../db/dblearntree.js", "w", encoding="utf8") as f:
    f.write("var zhuan_map_child =")
    f.write(str(zhuan_map_child))
    f.write(';\n')
    f.write("var zhuan_map_parent =")
    f.write(str(zhuan_map_parent))
    f.write(';')
    print("writing")
print(zhuan_map_child)
print(zhuan_map_child['27.8FA8'])
# print(zhuan_map_parent)
