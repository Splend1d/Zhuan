import json

with open("../db/fontmap.json","r") as f: # for debugging
	db = json.load(f)
with open('../db/main.json',"r") as f:
	dbm = json.load(f)
z2i = {}
for k,v in dbm.items():
	for z in v['fonts'][1]:
		z2i[z] = k
with open("../db/fontmap.js", "w", encoding="utf8") as f:
    f.write("var z2k =")
    f.write(str(db['z2k']))
    f.write(';\n')
    f.write("var h2z =")
    f.write(str(db['h2z']))
    f.write(';\n')
    f.write("var z2i =")
    f.write(str(z2i))
    f.write(';')