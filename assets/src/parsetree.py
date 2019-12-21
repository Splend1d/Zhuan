import json
import pickle as pkl

with open("../db/main.json","r") as f:
	dbmain = json.load(f)
print(dbmain['1'])
with open("../db/subchars.json","r") as f:
	subchars = json.load(f)
with open("../db/mainchars.json","r") as f:
	mainchars = json.load(f)
subchars = set(subchars)
print(len(subchars))
with open("../db/tree.pkl","rb") as f:
	dbt = pkl.load(f)
print(dbt)
print(len(dbt[0]))
with open("../db/font.pkl","rb") as f: # for debugging
	dbf = pkl.load(f)
zhuan_map_han = {k:v for (k,_,v) in dbf}
han_map_zhuan = {v:k for (k,_,v) in dbf}
print(len(zhuan_map_han))
# exclude subchars
original_connections = 0
new_connections = 0
dbfiltered = [{},{},{},{},{},{},{},{},{}]
for n,lvl in enumerate(dbt):
	for k,v in lvl.items():
		original_connections += len(v)
		if k in subchars:
			continue
		keep = []
		for word in v:
			if word not in subchars:
				keep.append(word)
		dbfiltered[n][k] = keep
		new_connections += len(keep)
print(original_connections)
print(new_connections)
p = dbfiltered[0]
get_parent = p
get_child = {}

for k, vs in p.items():
    for v in vs:
        try:
            get_child[v].append(k)
        except:
            get_child[v] = [k]

basic = []
for k, v in get_child.items():
    if len(v) == 1:
        basic.append(k)
print("basic elements:",basic)
print(len(basic))
print([zhuan_map_han[b] for b in basic])


for i, p in enumerate(dbfiltered[1:]):
    for k, vs in p.items():
        for v in vs:
            # print(v)
            # print(basic)
            if k in basic:
                try:
                    get_child[v].append(k)
                except:
                    stop()  # this should never happen
                    get_child[v] = [k]
                # print(get_child[v])
                # print(k, v)
#patch self
for w in mainchars:
	if w not in get_child:
		get_child[w] = [w]
		print("added:",zhuan_map_han[w])
	if w not in get_parent:
		get_parent[w] = [w]
		print("added2:",zhuan_map_han[w])
print(len(get_child))
print(len(get_parent))
#patch major
for w in mainchars:
	for w2 in dbmain.values():
		if w == w2['fonts'][1][0]:
			if dbmain[str(w2['major'])]['fonts'][1][0] not in get_child[w]:
				get_child[w].append(dbmain[str(w2['major'])]['fonts'][1][0])
				print(zhuan_map_han[w], "added child",zhuan_map_han[dbmain[str(w2['major'])]['fonts'][1][0]])
#get complexity of each node
complexity = {}
for w in get_child:
	complexity[w] = len(get_child[w])
print(complexity)
for k in get_child:
    get_child[k] = sorted(get_child[k],key = lambda v:(complexity[v],v),reverse = True)
for k in get_parent:
    get_parent[k] = sorted(get_parent[k],key = lambda v:(complexity[v],v))
with open("../db/treechild.json","w") as f:
	json.dump(get_child, f)
with open("../db/treeparent.json","w") as f:
	json.dump(get_parent, f)
