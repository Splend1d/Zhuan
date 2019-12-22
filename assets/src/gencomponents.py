import pickle as pkl
import json
with open("../db/majors_coverage.pkl", "rb") as f:
    dbcoverage = pkl.load(f)


with open("../db/freq100000.json","rb") as f:
    common = json.load(f)

with open("../db/main.json","r") as f:
    main = json.load(f)

with open("../db/treeparent.json","r") as f:
    parent = json.load(f)

with open("../db/fontmap.json","r") as f:
    fontmap = json.load(f)


n_parents_distribution = [0] * 10
filter_common = 10
filtered_select = []
filtered_q = {}
for k,v in dbcoverage.items():
    try:
        n_parents_distribution[int(v[1])-int(v[0])+1] +=1
    except:
        n_parents_distribution[-1] += 1
    
    #for i in range(int(v[0]),int(v[1])+1): // 加權用
    if int(v[1])-int(v[0])+1 >= filter_common:
        filtered_select.append(k)
        filtered_q[k] = v
print(n_parents_distribution)
n_parents_distribution = [0] * 20
common = [main[c]["fonts"][1][0] for c in common]
filter_2 = 13
filter_3 = 8
filtered_select_2 = []
filtered_select_3 = []
for k,ps in parent.items():
    if fontmap['z2h'][k] not in dbcoverage.keys():
        thisans = 0
        for p in ps:
            if p in common:
                thisans += 1

        try:
            n_parents_distribution[thisans] +=1
        except:
            n_parents_distribution[-1] += 1

        if thisans >= filter_2:
            filtered_select_2.append(k)
        elif thisans >= filter_3:
            filtered_select_3.append(k)
print(n_parents_distribution)

print(len(filtered_select))
print(len(filtered_select_2))
print(len(filtered_select_3))
with open("../db/components.js", "w", encoding="utf8") as f:
    
    f.write("var select_major =")
    f.write(str(filtered_select))
    f.write(';\n')
    f.write("var major_gen_q =")
    f.write(str(filtered_q))
    f.write(';\n')
    f.write("var select_2 =")
    f.write(str(filtered_select_2))
    f.write(';\n')
    f.write("var select_3 =")
    f.write(str(filtered_select_3))
    f.write(';\n')
    

print("finished writing")    