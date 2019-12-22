import json
import pickle as pkl

with open("../db/treeparent.json","r") as f:
	parent = json.load(f)

with open("../db/main.json","r") as f:
	main = json.load(f)

with open("../db/majors.pkl","rb") as f:
	majors = pkl.load(f)

with open("../db/freq100000.json","rb") as f:
	common = json.load(f)
common = [main[c]["han"][0] for c in common]
print(common)
s()
available = []
print(parent)
print(majors)