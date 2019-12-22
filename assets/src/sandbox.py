import pickle as pkl
import json

with open("../db/font.pkl","rb") as f:
	db = pkl.load(f)
print(db)