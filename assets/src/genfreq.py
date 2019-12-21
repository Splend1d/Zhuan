import json

with open("../db/freq3000.json", "r") as f:
    dbf = json.load(f)
with open("../db/main.json", "r") as f:
    db = json.load(f)

with open("../db/treechild.json", "r") as f:
    child = json.load(f)
with open("../db/treechild.json", "r") as f:
    parent = json.load(f)

print(dbf)

# change order by number of parts
z3000 = []
for k in dbf:
	z = db[k]['fonts'][1][0]
	z3000.append([z,k])
z3000_sorted = []
for z,k in z3000:
	if len(child[z]) == 1 and db[k]['major'] == k:
		z3000_sorted.append([z,k])
z3000_sorted = sorted(z3000_sorted,key = lambda v:v[1])

for z,k in z3000:
	if len(child[z]) == 1 and [z,k] not in z3000_sorted:
		z3000_sorted.append([z,k])
while(len(z3000_sorted)!=len(z3000)):
	newed = False
	for z,k in z3000:
		if [z,k] not in z3000_sorted:
			for c in child[z]:
				if c not in [x[0] for x in z3000_sorted]:
					break
				z3000_sorted.append([z,k])
				print("+")
				newed = True
	print(len(z3000_sorted))
print(z3000)

def3000 = []
for i in dbf:
	def3000.append([db[str(i)]['meaning'].replace(db[str(i)]["han"][0],'@'),db[str(i)]["han"][0]])
with open("../db/freq3000.js", "w", encoding="utf8") as f:
    f.write("var freq3000 =")
    f.write(str(z3000))
    f.write(';\n')
    f.write("var def3000 =") #masked
    f.write(str(def3000))
    f.write(';\n')

