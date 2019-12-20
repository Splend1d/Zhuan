import json
import os
import pandas as pd

kaiid_2000 = []
def_2000 = []
fontid_2000 = []
font_2000 = []
major_2000 = []

with open("../db/freq.json","r") as f:
	freq = json.load(f)
lvls = sorted(list(set(freq.values())))
for lvl in lvls:
	for ch in freq:
		if freq[ch] == lvl:
			kaiid_2000.append(int(ch))
print(sorted(kaiid_2000))

df = pd.read_csv('../db/db.csv')
dfimg = pd.read_csv('../db/dbimg.csv')
fontid_all = df["字體編號"]
font_all = dfimg["楷書字型"]
kaiid_all = df["楷書編號"]
font_map_fontid = {} 
kaiid_map_font = {} 
for d,f,k in zip(font_all,fontid_all,kaiid_all):
	if int(k[2:-2]) not in kaiid_map_font:
		font_map_fontid[d] = f
		kaiid_map_font[int(k[2:-2])] = d
print(font_map_fontid)
print(kaiid_map_font)


df2 = pd.read_csv('../db/database_meaning.txt',sep='\t')
kaiid_all2 = df2[df2.columns[0]]
def_all = df2[df2.columns[1]]
majors_all = df2[df2.columns[2]]
kaiid_map_def = {}
kaiid_map_major = {}
#TODO: check for duplicates, determine most common
for i,d,m in zip(kaiid_all2,def_all,majors_all):
	kaiid_map_def[int(i)] = d
	kaiid_map_major[int(i)] = m
print(kaiid_map_def)

unlist = set()
no_char_def = set()
no_char_def_chars = 0
flag = False
for w in kaiid_2000: # int
	print(w, "parsing")
	try:
		thisdef = kaiid_map_def[int(w)]
	except:
		print(w, "not in kaiid_map_def")
		unlist.add(w)
		continue
	else:
		# check for font img avalibility
		if not isinstance(thisdef, str):
			unlist.add(w)
			print(w, "not str")
			continue
		flag = False
		for c in thisdef:
			if c not in font_map_fontid:
				no_char_def.add(c)
				flag = True
		if flag:
			no_char_def_chars += 1

	try:
		thisdef = thisdef.replace(kaiid_map_font[w], "@")
	except:
		print(w, "not in kaiid_map_font")
		unlist.add(w)
		continue
	def_2000.append(thisdef)
	fontid_2000.append(font_map_fontid[kaiid_map_font[w]])
	major_2000.append(kaiid_map_major[w])
	font_2000.append(kaiid_map_font[w])
	print("sucess")
# unlist elements without definition, or cannot find image	
for u in unlist:
	try:
		kaiid_2000.remove(u) 
	except:
		continue
# check equal length
print(len(font_2000))
print(len(major_2000))
print(len(fontid_2000))
print(len(def_2000))
print(no_char_def)
print(no_char_def_chars) # 說文用字找不到
s()

imgs = os.listdir('../db/img')
#print(imgs)


print("cannot map ",len(no_char_def)," instances")

noimg = []
for I in fontid_2000:
	if str(I)+".png" not in imgs:
		noimg.append(d)
print(noimg)
for ni in noimg:
	idx = kaiid_2000.index(ni)
	print(kaiid_2000[idx])
	del kaiid_2000[idx]
	del def_2000[idx]
	del fontid_2000[idx]
	del major_2000[idx]
print(def_2000)
print(major_2000)
print(fontid_2000)
print(kaiid_2000)
print(len(kaiid_2000),len(def_2000),len(major_2000),len(fontid_2000))

with open("../db/db.js","w",encoding = "utf8") as f:
	f.write("var kai_qidx =")
	f.write(str(fontid_2000))
	f.write(';\n')
	f.write("var kai_ans =")
	f.write(str(font_2000))
	f.write(';\n')
	f.write("var kai_def =")
	f.write(str(def_2000))
	f.write(';\n')
	f.write("var kai_part =")
	f.write(str(major_2000))
	f.write(';\n')
	f.write("var kai_dict =")
	f.write(str(font_map_fontid))
	f.write(';')
