import json
import pandas as pd
with open('../db/treechild.json', 'r') as f:
    child = json.load(f)
with open('../db/treeparent.json', 'r') as f:
    parent = json.load(f)
components = {}



with open("../db/tree.js", "w", encoding="utf8") as f:
    f.write("var zhuan_map_child =")
    f.write(str(child))
    f.write(';\n')
    f.write("var zhuan_map_parent =")
    f.write(str(parent))
    f.write(';\n')
    f.write("var zhuans =")
    f.write(str(list(parent.keys())))
    f.write(';')
print("finished writing")
print(child)
print(child['27.8FA8'])
# print(zhuan_map_parent)
