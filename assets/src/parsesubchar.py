import json
with open("../db/main.json","r") as f:
	db = json.load(f)

print(db)
subchars = []
mainchars = []
for k,v in db.items():
	if len(v['fonts'][1])>1 :
		subchars += v['fonts'][1][1:]
	mainchars.append(v['fonts'][1][0])

print(len(subchars))
print(len(mainchars))
with open("../db/subchars.json","w") as f:
	json.dump(subchars,f)
with open("../db/mainchars.json","w") as f:
	json.dump(mainchars,f)