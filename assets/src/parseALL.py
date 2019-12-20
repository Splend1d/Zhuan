import pickle as pkl
with open("../db/database_word.pkl", "rb") as f:
    this_dict = pkl.load(f)

print(this_dict)