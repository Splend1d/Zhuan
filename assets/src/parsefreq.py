import pickle as pkl
import json
with open("../db/freq3000.pkl", "rb") as f:
    dbf = pkl.load(f)
with open("../db/freq100000.pkl", "rb") as f:
    dbf2 = pkl.load(f)
print(len(dbf))
with open("../db/main.json", "r") as f:
    db = json.load(f)
print(len(dbf))
freq_filter = []  # 不要異體字
freq_filter2 = []
for f in dbf:
    f = f[1:-1]
    flag = False
    for k, v in db.items():
        if v['fonts'][1][0] == f:
            freq_filter.append(k)
            flag = True
            break
        elif f in v['fonts'][1][1:]:
            if len(set(v['han'])) == 1:  # is 異體，but same 電腦字體，so無所謂
                freq_filter.append(k)
                break
for f in dbf2:
    f = f[1:-1]
    flag = False
    for k, v in db.items():
        if v['fonts'][1][0] == f:
            freq_filter2.append(k)
            flag = True
            break
        elif f in v['fonts'][1][1:]:
            if len(set(v['han'])) == 1:  # is 異體，but same 電腦字體，so無所謂
                freq_filter2.append(k)
                break
freq_filter = list(set(freq_filter))
freq_filter2 = list(set(freq_filter2))
print(freq_filter)
print(len(freq_filter))
with open("../db/freq3000.json", "w") as f:
    json.dump(freq_filter, f)
with open("../db/freq100000.json", "w") as f:
    json.dump(freq_filter2, f)
