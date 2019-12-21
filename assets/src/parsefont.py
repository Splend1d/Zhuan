import pickle as pkl
import json

with open("../db/font.pkl","rb") as f: # for debugging
	dbf = pkl.load(f)
with open("../db/mainchars.json","r") as f: # for debugging
	mainchars = json.load(f)
print(len(dbf))
zhuan_map_kai = {z:k for (z,k,_) in dbf}
print(len(zhuan_map_kai))
zhuan_map_han = {z:h for (z,_,h) in dbf}
print(len(zhuan_map_han))
han_map_zhuan = {h:z for (z,_,h) in dbf}
print(len(han_map_zhuan))
# fix order
han_map_zhuan = {}
for (z,_,h) in dbf:
	if h not in han_map_zhuan:
		han_map_zhuan[h] = z
	else:
		if z in mainchars:
			print(z)
			han_map_zhuan[h] = z

with open("../db/fontmap.json","w") as f: # for debugging
	json.dump({"z2k":zhuan_map_kai,"z2h":zhuan_map_han,"h2z":han_map_zhuan},f)
print(zhuan_map_han)
print(zhuan_map_kai)
print(han_map_zhuan)