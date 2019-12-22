import pickle as pkl
import json

with open("../db/main.json", "r") as f:
    dbword = json.load(f)

with open("../db/essential.js", "w", encoding="utf8") as f:
    f.write("var zhuanid_map_all =")
    f.write(str(dbword))
    f.write(';\n')