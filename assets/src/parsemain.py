import pickle as pkl
import json
with open("../db/main.pkl", "rb") as f:
    db = pkl.load(f)
print(len(db)) # 9831

with open("../db/majors_coverage.json", "r") as f:
    dbm = json.load(f)
print(len(dbm)) # 540

with open("../db/font.pkl", "rb") as f:
    dbf = pkl.load(f)
print(len(dbf))

for k,v in db.items():
    f_sep = [[],[]]
    for f in v['fonts']:
        f = f[1:-1]
        if int(f.split(".")[0]) >= 27:
            f_sep[1].append(f)
        else:
            f_sep[0].append(f)
    db[k]['fonts'] = f_sep

for k,v in dbm.items():
    for i in range(int(v[0]),int(v[1])+1):
        db[i]['major'] = v[0]

for k,v in db.items():
    db[k]['han'] = []
for (z,_,t) in dbf:
    if len(t) == 0:
        continue
    for k,v in db.items():
        if z == v['fonts'][1][0]:
            db[k]['han'] = [t] + db[k]['han']
        elif z in v['fonts'][1]:
            db[k]['han'].append(t)
for k,v in db.items():
    if(len(db[k]['han'])==0):
        print("error")
    if(len(set(db[k]['han']))>1):
        print("id",k,"has multiple han representations",db[k]['han'])
print(db)




with open("../db/main.json", "w") as f:
    json.dump(db,f)
#recheck
with open("../db/main.json", "r") as f:
    db = json.load(f)
for v in db.values():
    if 'major' not in v:
        print("err")