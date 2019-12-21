import json
import pickle as pkl


with open("../db/freq3000.pkl","rb") as f:
	db = pkl.load(f)
	print(len(db))