import pickle as pkl
import json
with open("../db/database_coverage.pkl", "rb") as f:
    dbcoverage = pkl.load(f)
with open("../db/database_word.json", "r") as f:
    dbword = json.load(f)

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

print(len(filtered_select))
with open("../db/dbcomponents.js", "w", encoding="utf8") as f:
    
    f.write("var select_major =")
    f.write(str(filtered_select))
    f.write(';\n')
    f.write("var major_gen_q =")
    f.write(str(filtered_q))
    f.write(';\n')
    
with open("../db/dbessential.js", "w", encoding="utf8") as f:
    f.write("var zhuanid_map_all =")
    f.write(str(dbword))
    f.write(';\n')
print("finished writing")    