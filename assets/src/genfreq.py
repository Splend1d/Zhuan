import json
with open("../db/main.json", "r") as f:
    db = json.load(f)
with open("../db/freq100000.json", "r") as f:
    db100000 = json.load(f)

z100000 = {db[e]['fonts'][1][0]: "" for e in db100000}


with open("../db/freq100000.js", "w", encoding="utf8") as f:
    f.write("var freq100000 =")
    f.write(str(z100000))
    f.write(';')

with open("../db/freq3000.json", "r") as f:
    dbf = json.load(f)


with open("../db/treechild.json", "r") as f:
    child = json.load(f)
with open("../db/treeparent.json", "r") as f:
    parent = json.load(f)
with open("../db/fontmap.json", "r") as f:  # for human eye evaluation
    fontmap = json.load(f)
print(len(dbf))

# change order by number of parts
# get zhuanid mapping
z3000 = []
unuseid = [x for x in range(1, 9832)]
for k in dbf:
    z = db[k]['fonts'][1][0]
    z3000.append([z, k])
    unuseid.remove(int(k))
print(len(unuseid))
zhuan2id = {db[k]['fonts'][1][0]: k for k in db}
# remove unused child
unusedzhuan = []
for k in unuseid:
    z = db[str(k)]['fonts'][1][0]
    unusedzhuan.append(z)
print(sum([len(c) for c in child]))
for z in unusedzhuan:
    del child[z]
print(sum([len(c) for c in child.values()]))


z3000_sorted = [[]]
depth = 0
rank = {k: len(v) for k, v in parent.items() if k in child}  # for sort
while(len(child) != 0):
    for z, k in z3000:
        try:
            if len(child[z]) == 1:
                z3000_sorted[depth].append([z, k])
                print("parsed", fontmap['z2h'][z], depth)

        except:
            pass  # already parsed
    news = [x[0] for x in z3000_sorted[depth]]
    for z in news:
        del child[z]
    for z in news:
        for k, v in child.items():
            child[k] = list(filter(lambda a: a != z, child[k]))
    if depth == 1:
        for z in unusedzhuan:
            for k, v in child.items():
                child[k] = list(filter(lambda a: a != z, child[k]))

    if (len(z3000_sorted[-1]) == 0):
        child_sort = sorted(list(child.keys()), key=lambda a: rank[a], reverse=True)
        z3000_sorted[depth].append([child_sort[0], zhuan2id[child_sort[0]]])
        # print(parent[child_sort[0]])
        print("parsed", fontmap['z2h'][child_sort[0]], depth)
        del child[child_sort[0]]
        for k, v in child.items():
            child[k] = list(filter(lambda a: a != child_sort[0], child[k]))
    depth += 1
    z3000_sorted.append([])
print(depth)
print([len(x) for x in z3000_sorted])
# print(child)
print(sum([len(x) for x in z3000_sorted]))

z3000_sorted_fine = [sorted(x, key=lambda v:v[1]) for x in z3000_sorted]
print(z3000_sorted_fine)
z3000 = []
for depth in z3000_sorted_fine:
    for e in depth:
        z3000.append(e[1])
print(len(z3000))

for n, i in enumerate(z3000):
    if i == "94":
        print(n)


def3000 = []
for i in z3000:
    def3000.append([db[str(i)]['meaning'].replace(db[str(i)]["han"][0], '@'), db[str(i)]["han"][0]])
with open("../db/freq3000.js", "w", encoding="utf8") as f:
    f.write("var freq3000 =")
    f.write(str(z3000))
    f.write(';\n')
    f.write("var def3000 =")  # masked
    f.write(str(def3000))
    f.write(';\n')
